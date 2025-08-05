from flask import Flask, request, jsonify
from flask_cors import CORS
from main import yt_in_best, audio_from_yt

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    dtype = data.get('type')  # 'video' or 'audio'
    if not url or dtype not in ('video', 'audio'):
        return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

    try:
        if dtype == 'video':
            yt_in_best(url)
        else:
            audio_from_yt(url)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

    