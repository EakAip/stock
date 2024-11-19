import akshare as ak

# 获取期货数据 以玻璃“FG2501”为例
futures_zh_minute_sina_df = ak.futures_zh_minute_sina(symbol="FG2501", period="5")

# 选择需要的列，并重命名列标题为中文
futures_zh_minute_sina_df = futures_zh_minute_sina_df[['时间', 'open', 'high', 'low', '收盘价']]
futures_zh_minute_sina_df.columns = ['时间', '开盘价', '最高价', '最低价', '收盘价']

# 将数据保存到当前目录下的 CSV 文件
futures_zh_minute_sina_df.to_csv("玻璃期货五分钟行情数据.csv", index=False)

print("数据已保存到当前目录下的 五分钟行情数据.csv 文件中，标题为中文")
