from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import logging
import os

app = Flask(__name__)
# 啟用 CORS，允許所有來源訪問（包括 file:// 協議）
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": False
    }
})

# 設定日誌
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'flask_app.log')

# 配置日誌格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8', mode='a'),
        logging.StreamHandler()  # 同時輸出到控制台
    ],
    force=True  # 強制重新配置
)

logger = logging.getLogger(__name__)
# 確保日誌立即寫入
for handler in logger.handlers:
    handler.flush()

# 啟動時記錄
logger.info('='*50)
logger.info('Flask 應用啟動')
logger.info(f'日誌檔案位置: {log_file}')
logger.info('='*50)

@app.route('/api/button-click', methods=['POST', 'OPTIONS'])
def button_click():
    # 處理 OPTIONS 預檢請求
    if request.method == 'OPTIONS':
        return '', 204
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', '未知')
    
    # 記錄詳細資訊
    logger.info(f'收到按鈕點擊！')
    logger.info(f'  時間: {timestamp}')
    logger.info(f'  來源 IP: {ip}')
    logger.info(f'  User-Agent: {user_agent}')
    
    # 強制刷新所有日誌處理器
    for handler in logger.handlers:
        handler.flush()
    
    return jsonify({
        'status': 'success',
        'message': '後端已收到',
        'timestamp': timestamp
    })

@app.route('/api/logs', methods=['GET', 'OPTIONS'])
def get_logs():
    """讀取最近的日誌（最新 50 行）"""
    # 處理 OPTIONS 預檢請求
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            recent_logs = lines[-50:]  # 最新 50 行
            return jsonify({
                'status': 'success',
                'logs': recent_logs
            })
    except Exception as e:
        logger.error(f'讀取日誌失敗: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # 0.0.0.0 讓服務可以從外部訪問
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False, threaded=True)