# 1. 查看當前服務狀態
sc query FlaskAppService

# 2. 強制終止 pythonservice.exe（服務進程）
taskkill /F /IM pythonservice.exe

# 3. 強制終止所有 python.exe（包括正在運行的 app.py）
taskkill /F /IM python.exe

# 4. 等待 5 秒讓系統清理
timeout /t 5

# 5. 刪除服務
sc delete FlaskAppService

# 6. 再等待 10 秒
timeout /t 10

# 7. 確認服務已刪除（應該顯示「找不到指定的服務」）
sc query FlaskAppService

# app.run(host='0.0.0.0', port=5000, debug=False)  # 服務模式用 False

# 1. 安裝服務
python flask_service.py install

# 2. 設定為自動啟動
python flask_service.py --startup auto install

# 3. 啟動服務
python flask_service.py start

# 4. 檢查服務狀態（應該顯示 STATE: 4 RUNNING）
sc query FlaskAppService

# 查看詳細狀態
Get-Service -Name FlaskAppService

# 測試 API 是否響應
curl http://127.0.0.1:5000/api/logs


# 查看服務狀態
sc query FlaskAppService

# 啟動服務
python flask_service.py start

# 停止服務
python flask_service.py stop

# 重啟服務（停止後再啟動）
python flask_service.py stop
timeout /t 3
python flask_service.py start

# 移除服務
python flask_service.py remove

# 檢查服務是否在運行