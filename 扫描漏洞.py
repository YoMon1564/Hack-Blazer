import requests

def scan_vulnerabilities(url):
    vulnerabilities = []
    
    # 示例：检查SQL注入漏洞
    sql_injection_url = url + "'"
    try:
        response = requests.get(sql_injection_url)
        if "You have an error in your SQL syntax" in response.text:
            vulnerabilities.append("SQL Injection Vulnerability")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # 示例：检查XSS漏洞
    xss_url = url + "<script>alert('XSS')</script>"
    try:
        response = requests.get(xss_url)
        if "<script>alert('XSS')</script>" in response.text:
            vulnerabilities.append("XSS Vulnerability")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return vulnerabilities

def main():
    target_url = input("Enter the target URL: ")
    vulnerabilities = scan_vulnerabilities(target_url)
    
    if vulnerabilities:
        print("Vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"- {vuln}")
    else:
        print("No vulnerabilities found.")

if __name__ == "__main__":
    main()
