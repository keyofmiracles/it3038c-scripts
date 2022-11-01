This is a python script that utilizes the wikipedia module to scrape content from Wikipedia articles. The main purpose of the script is to scrape and print out the studio albums listed on a musical artist's Wikipedia page. It works by using a specific command to scrape the Discography section from each artist's page and then prints it out. However, if the page was created with the albums listed under a subsection that is in turn under Discography, it will not return any values, so it does not work for all artist pages.

The program starts by asking what artist you want to search for. You type that value in and it searches for that artist's wikipedia page. It will list all the possible values in a disambiguation just like the website would, just in case you search for an artist and the search string brings up multiple wikipedia pages.

Then, it prints the text under the "Discography" section on their wikipedia page.
