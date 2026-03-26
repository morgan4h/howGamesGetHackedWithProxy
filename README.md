# 🎮 How Games Get Hacked Using a Proxy (Educational Project)

> ⚠️ **Disclaimer**
@created@by@sofai4h [SOFAI 4H](https://youtube.com/@SOFAI4H)
>
> This project is for **educational and research purposes only**.  
> It demonstrates how network traffic works and how vulnerabilities *can* be exploited — so developers and learners can better understand and **secure their systems**.  
> Do NOT use this knowledge to cheat or harm others.

---

## 📌 Overview

This project demonstrates how a **proxy-based attack** can be used to intercept and modify communication between a game client and its server.

In simple terms:

[ Game Client ] <---> [ Proxy (YOU) ] <---> [ Game Server ]


The proxy sits **in the middle** and can:
- 👀 Read traffic (requests & responses)
- ✏️ Modify data before it reaches the server
- 🔁 Replay or fake requests

This is similar to a **Man-in-the-Middle (MITM)** attack, where an attacker intercepts and manipulates communication. :contentReference[oaicite:0]{index=0}

---

## 🧠 How Proxy Attacks Work (Simple Explanation)

A **proxy server** acts as an intermediary between a client and a server.

Normally:

Client → Server → Response


With a proxy:


Because the proxy sees everything:
- It can **log traffic**
- It can **change values**
- It can **inject fake responses**

Attackers exploit this to:
- Modify game currency (coins, diamonds 💎)
- Change player stats (health, ammo)
- Bypass server validation
- Automate actions (bots)

👉 This works especially when:
- Data is **not encrypted**
- The server **trusts the client too much**
- There is **weak validation**

---

## ⚠️ Why Games Are Vulnerable

Some online games rely on client-side logic.

That means:
- The game sends requests like:  
  `{"action": "buy", "amount": 100}`
- If the server doesn’t verify properly → it trusts the request

A proxy can change it to:

{"action": "buy", "amount": 999999}


This is called **traffic manipulation**.

Research shows proxy-based attacks can:
- Intercept and modify application data
- Impersonate legitimate users
- Exploit weak security layers :contentReference[oaicite:1]{index=1}

---

## 🧰 Project Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/morgan4h/howGamesGetHackedWithProxy.git
cd howGamesGetHackedWithProxy



This is called **traffic manipulation**.

Research shows proxy-based attacks can:
- Intercept and modify application data
- Impersonate legitimate users
- Exploit weak security layers :contentReference[oaicite:1]{index=1}

---

## 🧰 Project Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/morgan4h/howGamesGetHackedWithProxy.git
cd howGamesGetHackedWithProxy

2️⃣ Open in VS Code

code .

3️⃣ Install Python

Download and install Python from:
👉 https://www.python.org/downloads/

Verify installation:    

python --version


4️⃣ Run the Project

Open the VS Code terminal and run:

python garenaFreeFireServer.py

python ccProxy.py

python yourPhone.py

@created@by@sofai4h [SOFAI 4H](https://youtube.com/@SOFAI4H)

==============================arabic===========================================


# 🎮 كيف يتم اختراق الألعاب باستخدام البروكسي (مشروع تعليمي)

> ⚠️ **إخلاء مسؤولية**
>
> هذا المشروع للأغراض **التعليمية والبحثية فقط**.  
> يهدف المشروع لتوضيح كيفية عمل حركة مرور الشبكة وكيف *يمكن* استغلال الثغرات — حتى يتمكن المطورون والمتعلمون من فهم **تأمين أنظمتهم** بشكل أفضل.  
> لا تستخدم هذه المعرفة للغش أو إيذاء الآخرين.

---

## 📌 نظرة عامة (Overview)

يوضح هذا المشروع كيف يمكن استخدام **هجوم قائم على البروكسي (Proxy-based attack)** لاعتراض وتعديل الاتصال بين مشغل اللعبة (Client) وخادمها (Server).

ببساطة:

`[ مشغل اللعبة ] <---> [ البروكسي (أنت) ] <---> [ خادم اللعبة ]`


يجلس البروكسي **في المنتصف** ويمكنه:
- 👀 قراءة حركة المرور (الطلبات والاستجابات)
- ✏️ تعديل البيانات قبل وصولها إلى الخادم
- 🔁 إعادة إرسال أو تزييف الطلبات

هذا مشابه لهجوم **رجل في المنتصف (Man-in-the-Middle - MITM)**، حيث يقوم المهاجم باعتراض وتلاعب الاتصالات.

---

## 🧠 كيف تعمل هجمات البروكسي (شرح مبسط)

يعمل **خادم البروكسي** كوسيط بين العميل والخادم.

في الحالة الطبيعية:
`العميل ← الخادم ← الاستجابة`

مع وجود بروكسي، ولأن البروكسي يرى كل شيء:
- يمكنه **تسجيل حركة المرور**
- يمكنه **تغيير القيم**
- يمكنه **حقن استجابات مزيفة**

يستغل المهاجمون ذلك لـ:
- تعديل عملات اللعبة (العملات المعدنية، الألماس 💎)
- تغيير إحصائيات اللاعب (الصحة، الذخيرة)
- تجاوز التحقق من جانب الخادم
- أتمتة الإجراءات (البوتات)

👉 يحدث هذا خاصة عندما:
- تكون البيانات **غير مشفرة**
- يثق الخادم في العميل **أكثر من اللازم**
- يكون هناك **تحقق ضعيف** من البيانات

---

## ⚠️ لماذا تكون الألعاب عرضة للاختراق

تعتمد بعض الألعاب عبر الإنترنت على المنطق البرمجي من جانب العميل (Client-side logic).

وهذا يعني:
- ترسل اللعبة طلبات مثل:  
  `{"action": "buy", "amount": 100}`
- إذا لم يقم الخادم بالتحقق بشكل صحيح ← فإنه يثق في الطلب

يمكن للبروكسي تغييره إلى:
`{"action": "buy", "amount": 999999}`

هذا ما يسمى **التلاعب بحركة المرور (Traffic Manipulation)**.

تظهر الأبحاث أن الهجمات القائمة على البروكسي يمكنها:
- اعتراض وتعديل بيانات التطبيق
- انتحال شخصية المستخدمين الشرعيين
- استغلال طبقات الأمان الضعيفة

---

## 🧰 إعداد المشروع (Project Setup)

### 1️⃣ استنساخ المستودع (Clone the Repository)

```bash
git clone [https://github.com/morgan4h/howGamesGetHackedWithProxy.git](https://github.com/morgan4h/howGamesGetHackedWithProxy.git)
cd howGamesGetHackedWithProxy

2️⃣ الفتح في VS Code
Bash
code .
3️⃣ تثبيت بايثون (Python)
قم بتحميل وتثبيت بايثون من:

👉 https://www.python.org/downloads/

تحقق من التثبيت:

Bash
python --version
4️⃣ تشغيل المشروع
افتح واجهة الأوامر (Terminal) في VS Code وقم بتشغيل الملفات التالية بالترتيب:

Bash
python garenaFreeFireServer.py
Bash
python ccProxy.py
Bash
python yourPhone.py

@created@by@sofai4h [SOFAI 4H](https://youtube.com/@SOFAI4H)