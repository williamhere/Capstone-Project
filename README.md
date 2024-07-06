# Capstone-Project
大學專題總結 
專題名稱：既有坐姿辨識功能之檯燈

指導教授：夏世昌 特聘教授

專題學生：曹宸維、陳維翔

專題背景：
現代生活中，兒童因長時間使用電子設備、不良的坐姿習慣及缺乏運動，容易出現姿勢不良的現象，尤其是駝背會影響骨骼發展。為了幫助兒童維持良好的坐姿並預防駝背問題，我們開發了一款具有坐姿辨識功能的智能檯燈。

專題目標：
開發一款智能檯燈，利用Raspberry Pi 4和Google Coral USB加速器，結合攝影機和檯燈，實現即時人體姿態偵測和駝背提醒功能。

技術特點：

即時人體骨架偵測：利用TensorFlow的PoseNet模型，即時從攝影機影像中精準偵測人體骨架，特別關注頭部、肩部和脊椎等關鍵部位。
駝背偵測功能：通過PoseNet提取的特徵值，運用特定演算法，即時辨識使用者是否存在駝背現象，並發出警示提醒調整坐姿。
即時反饋和提醒：檯燈具有即時反饋功能，當偵測到駝背時，會通過燈光變化、聲音提示等方式即時提醒，幫助使用者改善坐姿。
優化運行於Raspberry Pi：針對嵌入式系統的限制，優化了模型的運行效率和資源消耗，確保在Raspberry Pi等硬體上穩定高效運行。
未來展望：

個性化設定功能：允許家長根據兒童的特定需求和舒適度進行個性化設定。
數據追蹤和分析功能：檯燈可以記錄兒童坐姿的變化趨勢，提供有價值的信息，幫助家長更好地監測和改善兒童的健康狀態。

關鍵字：
姿勢偵測、駝背提醒、PoseNet
