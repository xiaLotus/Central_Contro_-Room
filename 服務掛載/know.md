# ===== 以系統管理員身份執行 PowerShell =====

# 切換目錄
cd C:\Users\User\Desktop\fkas

# 清理卡住的服務
Write-Host "步驟 1/7: 查看服務狀態..." -ForegroundColor Yellow
sc query FlaskAppService

Write-Host "`n步驟 2/7: 終止 pythonservice.exe..." -ForegroundColor Yellow
taskkill /F /IM pythonservice.exe 2>$null

Write-Host "`n步驟 3/7: 終止所有 python.exe..." -ForegroundColor Yellow
taskkill /F /IM python.exe 2>$null

Write-Host "`n步驟 4/7: 等待 5 秒..." -ForegroundColor Yellow
timeout /t 5 /nobreak | Out-Null

Write-Host "`n步驟 5/7: 刪除服務..." -ForegroundColor Yellow
sc delete FlaskAppService

Write-Host "`n步驟 6/7: 等待 10 秒..." -ForegroundColor Yellow
timeout /t 10 /nobreak | Out-Null

Write-Host "`n步驟 7/7: 確認服務已刪除..." -ForegroundColor Yellow
sc query FlaskAppService

Write-Host "`n===== 清理完成！現在可以重新安裝服務 =====" -ForegroundColor Green
Write-Host "請確認 app.py 中使用 debug=False，然後執行：" -ForegroundColor Cyan
Write-Host "python flask_service.py install" -ForegroundColor White
Write-Host "python flask_service.py start" -ForegroundColor White

快速參考卡
常用服務管理命令
powershell# 查看服務狀態
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
Get-Service -Name FlaskAppService
緊急終止命令
powershell# 強制終止服務進程
taskkill /F /IM pythonservice.exe

# 強制終止所有 Python
taskkill /F /IM python.exe

注意事項
⚠️ 執行 taskkill /F /IM python.exe 會關閉：

正在運行的 python app.py
任何其他正在運行的 Python 程式
不會影響 Python 軟體本身

✅ 執行完 taskkill 後可以立即：

重新執行 python app.py
安裝新的服務
使用 Python 做任何事


把這份清單存起來，以後需要管理服務時就很方便了！ 😊RetryClaude can make mistakes. Please double-check responses.