import requests

def search_github(username):
    url = f'https://github.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_twitter(username):
    url = f'https://twitter.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_instagram(username):
    url = f'https://www.instagram.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_facebook(username):
    url = f'https://www.facebook.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_linkedin(username):
    url = f'https://www.linkedin.com/in/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_reddit(username):
    url = f'https://www.reddit.com/user/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_tiktok(username):
    url = f'https://www.tiktok.com/@{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_snapchat(username):
    url = f'https://www.snapchat.com/add/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_pinterest(username):
    url = f'https://www.pinterest.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_whatsapp(username):
    url = f'https://wa.me/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_telegram(username):
    url = f'https://t.me/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_youtube(username):
    url = f'https://www.youtube.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_messenger(username):
    url = f'https://www.messenger.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_wechat(username):
    url = f'https://www.wechat.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_qq(username):
    url = f'https://www.qq.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_sina_weibo(username):
    url = f'https://www.weibo.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_qzone(username):
    url = f'https://www.qzone.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_douyin(username):
    url = f'https://www.douyin.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def search_kuaishou(username):
    url = f'https://www.kuaishou.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return url
    else:
        return None

def main():
    username = input("Enter the username to search for: ")
    print("Searching...")

    results = {
        'GitHub': search_github(username),
        'Twitter': search_twitter(username),
        'Instagram': search_instagram(username),
        'Facebook': search_facebook(username),
        'LinkedIn': search_linkedin(username),
        'Reddit': search_reddit(username),
        'TikTok': search_tiktok(username),
        'Snapchat': search_snapchat(username),
        'Pinterest': search_pinterest(username),
        'WhatsApp': search_whatsapp(username),
        'Telegram': search_telegram(username),
        'YouTube': search_youtube(username),
        'Messenger': search_messenger(username),
        'WeChat / Weixin': search_wechat(username),
        'QQ': search_qq(username),
        'Sina Weibo': search_sina_weibo(username),
        'Qzone': search_qzone(username),
        'Douyin': search_douyin(username),
        'Kuaishou': search_kuaishou(username)
        # Add more platforms here...
    }

    print("\nSearch Results:")
    for platform, url in results.items():
        if url:
            print(f" - {platform}: {url}")
        else:
            print(f" - {platform}: Profile not found")

if __name__ == "__main__":
    main()
