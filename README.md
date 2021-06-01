# <a href="https://github.com/tobeaprogrammer/AmazonProductMonitor_Python/edit/main/README.md">Product Price Monitor for Amazon</a>

<div>
  <h5><div name="title">
    Project Description : The Python Program uses a JSON input and checks for the prices of the prodcuts based on the URL provided. If the price is lower than the price provided in the JSON, it will send a email with price change details and the URL to the mentioned email id. For the Project to be able to send email add the email credentials in the JSON/cred.json File. The Prodcuts to monitor will be added in the JSON/products.JSON in the name, url, price format. The ProductMonitor_Amazon.py file contains the code to perform all the operations. This can be mapped to a task in the task scheduler or a job on jenkins. [Recommended : Triggered every 24 hours]
    </div></h5>
  <div name="setup">
    Setup : <br/>
    <ol>
        <li> JSON / cred.json -> Enter the email credentails
        <li> JSON / products.json -> Enter the product details in the format [sample provided]
        <li> utilities / MailOperations.py -> Enter the Recievers Email in the SendEmail functions optional argument
    </ol>
  </div>
 </div>
<table>
  <tr><td><b>Programming Language</b></td><td>Python</td></tr>
  <tr><td><b>Project Output</b></td><td>Email if conditions are true</td></tr>
  <tr><td><b>Data Source</b></td><td>JSON</td></tr>
  <tr><td><b>Credential Source</b></td><td>JSON</td></tr>
  <tr><td><b>Packages Used</b></td><td>Selenium, smtplib, json, MIMEMultipart </td></tr>
</table>
</div>
