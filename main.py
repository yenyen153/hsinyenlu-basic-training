#%%
## 執行參數設定與使用原因
## 1. 點選右上角專案名稱
## 2. 找到Edit Configurations
## 3. 找到script parameters並輸入指定parameters

## 設定parameters原因:
## 雖然使用terminal也可以指定參數，但每次執行都必須重新輸入，當某些參數可以鎖死不需要每次都輸入時，直接在pycharm設定即可
## 優點在於，使用pycharm鎖死參數，可以避免浪費每次都要重新輸入的時間，若要更改參數時，也可透過pycharm中內部設定做更改，不會直接更改到主程式

## 以下為例
import argparse

parser = argparse.ArgumentParser(description="orders")

parser.add_argument("--food", required=str, help="輸入食物名稱")
parser.add_argument("--drink", required=str, help="輸入飲料名稱")
parser.add_argument("--side", required=str, help="輸入附餐名稱")

args = parser.parse_args()

print(f"我要一份:{args.food}、{args.drink}附餐要{args.side}!")

#%%
## 設定環境變數的方法與原因
## 1. 點選右上角專案名稱
## 2. 找到Edit Configurations
## 3. 找到 Environment Variables
## 4. 即可進入編輯環境變數

## 設定環境變數原因:
## 當主程式需用到密碼或API金鑰時，可將這些訊息存放在環境變數中，優點是可以使專案在不同電腦中，都能透過讀取統一的環境變數來操作
## 另外在專案開發時，常會使用DEBUG模式，但正式發布時須將DEBUG關閉，可將DEBUG設為環境變數之一，使專案更好控制DEBUG開關

## 以下為例
import os

api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")

print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")