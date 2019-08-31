# psyco-emailsender
python script for sending an email from a postgresql table whenever a new row is added
Sends an email with the contents of latest row added. In this case the main table had 2 columns, currently the script wouldn't work otherwise. Might fix in the future using a simple function.

<h2>Instructions</h2>
Download it and edit the details to your specifications. Run it in the background. 

<h2>CloudSQL</h2>
This works if you run your db on your own server. If you need a solution for cloudsql this works if you replace 'localhost' with the servers address. It's still rather inefficient but is the only soulution as cloudsql are kind of bastardly in their refusal to integrate plpython3u.
