
# Working with: https://httpbin.org/#/Dynamic_data
#==================================================================================================================================#

import requests  # Importing the requests library to handle HTTP requests in Python.

# Usage of HTTP methods:
# GET - Used to retrieve information about a resource.
# POST - Used to create or upload a new resource.
# PUT - Used to completely update an existing resource.
# PATCH - Used to partially update specific aspects of a resource.
# DELETE - Used to remove a resource.

#==================================================================================================================================#

response = requests.get("https://httpbin.org/get")  # Sending a GET request to the specified URL.
print(response.status_code)  # Checking the status code to ensure the request was successful (200 means OK).
print(response.text)  # Printing the full content of the response.

# Converting the response to a JSON object so that we can work with it as a dictionary.
# The API's response is JSON, which can be easily converted to a Python dictionary.
res_json = response.json()

# If you don't want to print your IP address (which is shown under the 'origin' key):
del res_json['origin']  # Deleting the 'origin' key from the dictionary.
print(res_json)  # Printing the modified JSON response.

#==================================================================================================================================#

# Often, you will have the option to include query parameters in your URL.
response = requests.get("https://httpbin.org/get?name=mike&age=25")  # Sending a GET request with query parameters.
print(response.text)  # Printing the full content of the response.

#==================================================================================================================================#

# You can add query parameters without manually formatting the URL.
# We can pass parameters as a dictionary, which will be automatically formatted into the URL.

params_toAdd = {
    'name': 'shalom',
    'age': 20
}

# Adding query parameters using a dictionary:
response = requests.get("https://httpbin.org/get", params=params_toAdd)
# To see the resulting URL with the query parameters:
print(response.url)
print(response.text)  # Printing the full content of the response.

#==================================================================================================================================#

# Now, let's create a POST request:
# It works a bit differently: instead of sending data as query parameters, we send it as form data using the 'data' argument.

payload = {
    'name': 'moses',
    'age': 83
}

response = requests.post("https://httpbin.org/post", data=payload)
print(response.url)  # Printing the URL of the request.
print(response.text)  # Printing the full content of the response.
# We can see that there are no query parameters, but the data we posted appears in the form section.

#==================================================================================================================================#

# Let's see how to handle different status codes:
# When exploring APIs, you might automate processes that could occasionally cause errors.
# In such cases, you might encounter specific status codes that indicate problems.
# We can send requests to different status endpoints to see how they behave.

response = requests.get("https://httpbin.org/status/200")
print(response.status_code)  # Checking if the status code is 200 (OK).

response = requests.get("https://httpbin.org/status/404")
print(response.status_code)  # 404 indicates "Not Found". We see the status code reflects the input URL.

# If the response status code is 404 (not found).
# we can handle it without memorizing the code:
if response.status_code == requests.codes.not_found:
    print("Not found")
else:
    print(response.status_code)

#==================================================================================================================================#

# Sometimes you want to change the User-Agent, which identifies the software making the request.

response = requests.get("https://httpbin.org/user-agent")
print(response.text)  # By default, the User-Agent is "python-requests/2.31.0".
# Websites may block requests based on the User-Agent because it identifies your software as a Python script rather than a web browser.
# We can manually specify a different User-Agent:

headers_ToADD = {
    "User-Agent": "HelloWorld/1.1",  # Custom User-Agent string.
    "Accept": "image/png"  # Specify the file type you want to accept in the response.
}

response = requests.get("https://httpbin.org/user-agent", headers=headers_ToADD)
print(response.text)  # Now the User-Agent will be "HelloWorld/1.1".

response = requests.get("https://httpbin.org/image", headers=headers_ToADD)
print(response.text)  # The response is in bytes, so we need to convert it into a file.

with open("myimage.png", "wb") as f:
    f.write(response.content)  # Saving the response content as an image file.

#==================================================================================================================================#
# When working with a list of free public proxies, you might want to test which ones are functional.
# This can be done by using the proxies to send a request to a simple website and checking if it works.
# Sometimes, you won't get an immediate exception, but the response might take a long time (e.g., 2 minutes),
# indicating that the proxy is slow or not working properly.
# In such cases, you can specify a timeout period. If the response doesn't arrive within that time,
# an exception will be raised, allowing you to move on to the next proxy.

for _ in [1, 2, 3]:
    try:
        response = requests.get("https://httpbin.org/delay/5", timeout=3)  # The URL delays for 5 seconds, but the timeout is set to 3 seconds, which will raise an exception.
        res_json = response.json()
        print(res_json)
    except:
        continue  # If a timeout occurs, the code will skip to the next iteration without raising an exception.

#==================================================================================================================================#
# How to use a proxy server to send a request:
# Instead of sending a request directly to "httpbin", you send the request to the proxy server.
# The proxy server then forwards the request to "httpbin" on your behalf.

my_proxies = {
    "http": "139.99.237.62:80",
    # "https": "139.99.237.62:80"  # Uncomment this line if you want to use the proxy for HTTPS requests as well.
}

response = requests.get("https://httpbin.org/get", proxies=my_proxies)  # Sending the request through the proxy server.
print(response.text)  # The response should show the "origin" as the IP address of the proxy server, not your own.

# Explanation: 
# If the "origin" field in the response doesn't change, it could be because:
# 1. The proxy server is not working correctly, or it is not forwarding the request as expected.
# 2. The request might have bypassed the proxy, possibly due to incorrect proxy settings or a non-functional proxy.
# 3. If using HTTPS and the proxy is only set for HTTP, the request won't go through the proxy.

# Note: Ensure that the proxy server is functional and correctly configured to handle requests. 

##==================================================================================================================================#    


