# 替代役新訓考古題整理

**注意！** 這份整理只是把過去學長們分享的考古集結成一份、並去除重複題目；並 **沒有** 檢查過答案是否合乎新版法規。

對於正確解答，請參照[相關規定](#參考資料)，如果你願意協助更新題目或答案，歡迎[發PR](https://github.com/tzing/SMS-sample-question/pull/new/master)或[開issue](https://github.com/tzing/SMS-sample-question/issues)。


## 題目

- [是非題](./true_and_false.md)
- [選擇題](./multiple_choice.md)


## 題目來源

題目基於 [#1OouwokT (SMSlife)](https://www.ptt.cc/bbs/SMSlife/M.1489735346.A.B9D.html) 整理之，再加上後續少數的更新

| 代碼       | 標題 | 作者 |
|-----------|------|-----|
| #1G4xmgqv | [情報] 新訓考古題+法規整理 | q9898q
| #1GIBOKCJ | [情報] 111 梯新訓學科考試重點 | Popojjdd
| #1HUzCrUH | [心得] 118 梯次基礎訓練考古題 | ZEOR
| #1HSO6oLt | [情報] 新訓考古題資料(法規部分修版) | Jskblack
| #1KlEDuGh | [心得] 134T&136T 考古好讀版兼新訓考試心得分享 | shou50
| #1KvySzdQ | [心得] 替代役新訓超簡易攻略:行前準備篇 | january20
| #1KfaFEXp | [問題] 新訓該在外面準備/裏面買的東西 | Hevak
| #1LlGOCvO | [心得] 153T 替代役新訓超完整介紹 文長(含 153 考古題) | Ckchia
| #1LroM2F_ | [心得] 154T 學科測驗題目 | DecemberLV
| #1Ls6w2Gs | Re: [心得] 154T 學科測驗題目(答案) | aron77
| #1Lzfy4dP | [情報] 156T登入 新訓考古題整 | s0009s
| #1MVMQCPY | [情報] 160T 新訓考古題補充 | culturesky
| #1MsI2x6d | [心得] 161T新訓考古概略 | diding
| #1NDS0DLu | [心得] 163T成功嶺考古題暨教? | zerocoke
| #1OouwokT | [心得] 考古題統整(排版過) | paul22707808
| #1PVO1x20 | [心得] 179T新訓新增考古題 | young60509


## 參考資料

- [替代役實施條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040017)
    - [停役替代役役男免予回役作業規定](http://glrs.moi.gov.tw/LawContent.aspx?id=FL019351)
- [替代役役男獎懲辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040028)
- [替代役役男請假規則](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040021)
- [替代役役男權利實施辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040024)
- [替代役役男輔導教育辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040019)
- [替代役役男保險實施辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040027)
- [替代役役男撫卹實施辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040025)
- [替代役役男就醫醫療費用補助作業規定](http://www.rootlaw.com.tw/LawArticle.aspx?LawID=A040040051003300-1050629)
- [替代役實施條例施行細則](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040018)
- [一般替代役役男訓練服勤管理辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040020)
- [服兵役役男家屬生活扶助實施辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0040032)
- [內政部役政署替代役軍事基礎訓練成績評比規定](http://www.rootlaw.com.tw/LawArticle.aspx?LawID=A040040051006300-1060303)


## 腳本

`check.py` 是一個用於檢查是否有重複題目的腳本，它只能做最基本的文本比對；需要 Python 3.5 以上版本以執行，使用方式為

```bash
python check.py <FILE_NAME>
```

`FILE_NAME` 可為 *true_and_false.md* 或 *multiple_choice.md*，基本上接近於寫死用於這兩支檔案。
