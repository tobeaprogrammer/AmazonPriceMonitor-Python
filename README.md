# <a href="https://github.com/tobeaprogrammer/AmazonProductMonitor_Python/edit/main/README.md">Product Price Monitor for Amazon</a>

<div>    
    <h3><u><i>Project Description :</u></i></h3>
    <p style ="text-indent:40px"> 
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Python Program uses a JSON input and checks for the prices of the prodcuts based on the URL provided. If the price is lower than the price provided in the JSON, it will send a email with price change details and the URL to the mentioned email id. The ProductMonitor_Amazon.py file contains the code to perform all the operations. This can be mapped to a task in the task scheduler or a job on jenkins. [Recommended : Triggered every 24 hours]. The Input files are in the JSON folder. 
    </p>
    <br/>
  <div name="setup">
    <h3><u><i>Project Setup :</u></i></h3>
    <ol>
        <li> JSON / cred.json -> Enter the email credentails
        <li> JSON / products.json -> Enter the product details in the format [sample provided]
        <li> utilities / MailOperations.py -> Enter the Recievers Email in the 'SendEmail' functions optional argument
    </ol>
  </div>
 </div><br/>
 
 <h3><u><i>Project Details :</u></i></h3>
<table>
  <tr><td><b>Programming Language</b></td><td>Python</td></tr>
  <tr><td><b>Project Output</b></td><td>Email if conditions are true</td></tr>
  <tr><td><b>Data Source</b></td><td>JSON</td></tr>
  <tr><td><b>Credential Source</b></td><td>JSON</td></tr>
  <tr><td><b>Packages Used</b></td><td>Selenium, smtplib, json, MIMEMultipart </td></tr>
</table>
</div>
