import os
import sys
import uuid
import urllib.parse
import webbrowser
from threading import Timer
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from g4f.client import Client

app = Flask(__name__, static_folder='.')
CORS(app)

client = Client()

DETAILED_SYSTEM_PROMPT = (
    "You are Kilobyte AI, an intelligent, helpful assistant. "
    "Always provide comprehensive, detailed, and clear explanations. "
    "Avoid extremely short summaries or single-sentence answers. Expand on key points, "
    "provide context, and use examples or code blocks where applicable."
)

chats = {}

def get_ai_response(messages_payload, model_type):
    if model_type == 'claude':
        model_chain = ["claude-3.5-sonnet", "gpt-4o", "gemini-2.0-flash"]
    else:
        model_chain = ["gemini-2.0-flash", "gpt-4o-mini", "claude-3.5-sonnet"]

    for model_name in model_chain:
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages_payload,
                timeout=15
            )
            content = response.choices[0].message.content
            if content and len(content.strip()) > 0:
                return content
        except Exception as e:
            print(f"[Warning] Model {model_name} failed: {e}. Trying fallback...")
            continue

    raise Exception("All AI model providers are currently unresponsive. Please try again in a moment.")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json or {}
    prompt = data.get('prompt', '').strip()
    model_type = data.get('model', 'gemini')
    chat_id = data.get('chat_id')

    if not prompt:
        return jsonify({"error": "Empty prompt provided."}), 400

    if not chat_id or chat_id not in chats:
        chat_id = str(uuid.uuid4())
        chats[chat_id] = {
            "title": prompt[:30] + ("..." if len(prompt) > 30 else ""),
            "messages": []
        }

    session = chats[chat_id]

    if model_type == 'chatgpt':
        try:
            encoded_prompt = urllib.parse.quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
            
            image_html = f"""
<div style="margin-top: 10px;">
    <p><strong>Generated Image:</strong></p>
    <img src="{image_url}" alt="{prompt}" style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
</div>
"""
            session["messages"].append({"role": "user", "content": prompt})
            session["messages"].append({"role": "assistant", "content": image_html})
            
            return jsonify({
                "response": image_html,
                "chat_id": chat_id,
                "title": session["title"]
            })
        except Exception as e:
            return jsonify({"error": f"Image generation failed: {str(e)}"}), 500

    session["messages"].append({"role": "user", "content": prompt})
    messages_payload = [{"role": "system", "content": DETAILED_SYSTEM_PROMPT}] + session["messages"]

    try:
        answer = get_ai_response(messages_payload, model_type)
        session["messages"].append({"role": "assistant", "content": answer})
        
        return jsonify({
            "response": answer,
            "chat_id": chat_id,
            "title": session["title"]
        })
        
    except Exception as e:
        session["messages"].pop()
        return jsonify({"error": str(e)}), 500

@app.route('/chats', methods=['GET'])
def get_chats():
    chat_list = [{"id": cid, "title": cdata["title"]} for cid, cdata in chats.items()]
    return jsonify({"chats": chat_list[::-1]})

@app.route('/chats/<chat_id>', methods=['GET'])
def get_chat_history(chat_id):
    if chat_id in chats:
        return jsonify(chats[chat_id])
    return jsonify({"error": "Chat not found"}), 404

@app.route('/clear', methods=['POST'])
def clear_all():
    global chats
    chats = {}
    return jsonify({"status": "cleared"})

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(host='127.0.0.1', port=5000, debug=False, threaded=True)
