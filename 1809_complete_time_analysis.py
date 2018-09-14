import pandas as pd
import matplotlib.pyplot as plt
import os
#このコードがあるフォルダに移動
os.chdir('/Users/yt/analyze')
os.getcwd()

data_raw = pd.read_csv("data/covered_subject_users_and_times.csv", names = ("org_name", "userID", "subjects", "time_raw"))
data_raw.shape
data = data_raw.copy()

# コーチID（c01, c02で終わるID）を削除
# data.userID[data.userID.str.endswith("c01") == True]
data = data[data.userID.str.endswith("c01") == False]
data.shape#いくつ削除されたか、をshapeで確認

# テストorg、adminorgを削除
data = data[data.org_name != "admin"]
data = data[data.org_name.str.contains("test") == False]
data.shape
# data["org_name"] = data.org_name[data.org_name.str.contains("admin")]

time_1 = data.time_raw.str.replace("時間", "_").str.replace("分", "_").str.rstrip("秒")
#Sceriesに対してreplaceとかを実行する場合はstr.をつける
time = time_1.str.split("_", expand=True)

data["time(m)"] = time.iloc[:,0].astype(int) * 60 + time.iloc[:,1].astype(int)
data

# 科目ごとにDFを分ける
# ー＞timeのmax, min, ave, median,stdを算出

sorted(data.subjects.drop_duplicates())#重複削除し、各科目を並べてみる

# %% cell 1
data_cal["count"] = data.groupby("subjects")["time(m)"].count()
data_cal["mean"] = data.groupby("subjects")["time(m)"].mean().astype(int)
data_cal["min"] = data.groupby("subjects")["time(m)"].min()
data_cal["Max"] = data.groupby("subjects")["time(m)"].max()
data_cal["std"] = data.groupby("subjects")["time(m)"].std()
# data_cal = data_cal.drop("time(m)", axis=1)
data_cal
data_cal.to_excel("result_0911.xlsx")

# %% cell2
# ヒストグラムを書く。ダラダラ書いており、この下にもっと良いやつがある。一応残しとく。
# fig = plt.figure(figsize=(12,6))
#
#
# time_by_sub.head()
# ax1 = fig.add_subplot(231)
# plt.ylim([0, 30])
# ax2 = fig.add_subplot(232)
# plt.ylim([0, 30])
# ax3 = fig.add_subplot(233)
# plt.ylim([0, 30])
# ax4 = fig.add_subplot(234)
# plt.ylim([0, 30])
# ax5 = fig.add_subplot(235)
# plt.ylim([0, 30])
#
#
# ax1.hist(data[data.subjects == "math_1"]["time(m)"])
# ax1.set_title("math_1")
# ax1.set_xlabel('time(m)')
# ax2.hist(data[data.subjects == "math_2"]["time(m)"])
# ax2.set_title("math_2")
# ax2.set_xlabel('time(m)')
# ax3.hist(data[data.subjects == "math_3"]["time(m)"])
# ax3.set_title("math_3")
# ax3.set_xlabel('time(m)')
# ax4.hist(data[data.subjects == "math_a"]["time(m)"])
# ax4.set_title("math_a")
# ax4.set_xlabel('time(m)')
# ax5.hist(data[data.subjects == "math_b"]["time(m)"])
# ax5.set_title("math_b")
# ax5.set_xlabel('time(m)')
# # plt.legend()
#
# plt.tight_layout()
# plt.savefig("histgram.png")
# plt.show()
#
#
# sorted(data["subjects"].drop_duplicates())

# %% offg created


# subjects = ['chemistry_basic',
#  'chemistry_standard',
#  'en_grammar_advanced',
#  'en_grammar_advanced_plus',
#  'en_grammar_etc',
#  'en_grammar_fundamental',
#  'en_grammar_fundamental_plus',
#  'math_1',
#  'math_2',
#  'math_3',
#  'math_a',
#  'math_b',
#  'math_basic',
#  'math_elementary',
#  'physics_basic']
# ↓　data.subjectsから重複削除すればもっと短くできる
subjects = sorted(data.subjects.drop_duplicates())

plt.clf()
fig = plt.figure(figsize=(30,20))

for index, subject in enumerate(subjects, 1):#enumerateにより、各subjectの番号も取れるので、グラフ位置の特定に使える
    ax = fig.add_subplot(5, 3, index)#ここで5x3のパレット、というように指定
    ax.hist(data[data.subjects == subject]["time(m)"])
    ax.set_title(subject)
    ax.set_xlabel('time(m)')
    plt.ylim([0, 30])

plt.tight_layout()
# plt.savefig("histgram.png")
plt.show()

# %% offg created
