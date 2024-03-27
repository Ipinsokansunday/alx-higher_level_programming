##0x10. Python - Network #0
#Learning Objectives
What a URL is
What HTTP is
How to read a URL
The scheme for a HTTP URL
What a domain name is
What a sub-domain is
How to define a port number in a URL
What a query string is
What an HTTP request is
What an HTTP response is
What HTTP headers are
What the HTTP message body is
What an HTTP request method is
What an HTTP response status code is
What an HTTP Cookie is
How to make a request with cURL
What happens when you type google.com in your browser (Application level)
What a URL is:

URL stands for Uniform Resource Locator. It is a reference or address used to identify resources on the internet, such as web pages, images, files, etc. A URL typically consists of a protocol (e.g., HTTP, HTTPS), domain name (or IP address), path, and optional query parameters.
What HTTP is:

HTTP stands for Hypertext Transfer Protocol. It is an application protocol used for transmitting hypermedia documents, such as HTML. HTTP governs the communication between web clients (such as browsers) and servers.
How to read a URL:

A URL is typically read from left to right. It starts with the protocol (e.g., HTTP), followed by the domain name or IP address, then the path to the resource on the server, and finally, any query parameters.
The scheme for an HTTP URL:

The scheme for an HTTP URL specifies the protocol used for communication. For example, "http://" indicates the HTTP protocol, while "https://" indicates the secure version, HTTPS.
What a domain name is:

A domain name is a human-readable label that serves as an address for websites on the internet. It typically consists of a series of labels separated by dots (e.g., example.com).
What a sub-domain is:

A subdomain is a subset of a larger domain. It is used to organize and navigate within a domain hierarchy. For example, in "subdomain.example.com," "subdomain" is the subdomain.
How to define a port number in a URL:

A port number in a URL is specified after the domain name, separated by a colon. For example, "http://example.com:8080" specifies port 8080 for the HTTP connection.
What a query string is:

A query string is a part of a URL that follows a question mark (?). It consists of key-value pairs separated by ampersands (&), used to send data to a web server for processing.
What an HTTP request is:

An HTTP request is a message sent from a client to a server, requesting a specific action, such as retrieving a web page or submitting form data.
What an HTTP response is:

An HTTP response is a message sent from a server to a client in response to an HTTP request. It contains the requested resource or information about the status of the request.
What HTTP headers are:

HTTP headers are additional pieces of information sent along with HTTP requests or responses. They contain metadata about the message, such as content type, cache-control directives, authentication credentials, etc.
What the HTTP message body is:

The HTTP message body is the content of an HTTP request or response. It contains the actual data being sent or received, such as HTML content, JSON data, files, etc.
What an HTTP request method is:

An HTTP request method indicates the desired action to be performed on a resource. Common request methods include GET (retrieve data), POST (submit data), PUT (update data), DELETE (delete data), etc.
What an HTTP response status code is:

An HTTP response status code indicates the result of an HTTP request. It provides information about whether the request was successful, encountered an error, or requires further action. Examples include 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc.
What an HTTP Cookie is:

An HTTP cookie is a small piece of data sent from a web server to a web browser, which is stored locally by the browser. Cookies are commonly used for session management, user authentication, tracking user behavior, etc.
How to make a request with cURL:

cURL is a command-line tool for transferring data with URLs. To make a request with cURL, you would typically use the curl command followed by the URL you want to request. Additional options can be specified to customize the request, such as request headers, request methods, etc.
What happens when you type google.com in your browser (Application level):

When you type "google.com" in your browser and press Enter, your browser initiates an HTTP request to the server hosting Google's website. The server responds with the requested web page, which is then rendered by your browser for you to interact with. This process involves DNS resolution to translate the domain name into an IP address, establishing an HTTP connection, sending the HTTP request, receiving the HTTP response, and rendering the web page.
