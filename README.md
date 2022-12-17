# CS 340 - Client Server using Dash and MongoDb
### How do you write programs that are maintainable, readable, and adaptable? 
Programs are maintainable when each feature/function has one purpose and comments explain the purpose, inputs, and outputs. 
Programs are readable when the syntax is consistently formatted, and comments added to code if the purpose of the code isn't clear from the overall context. 
Code is adaptable when more functionalities can be added without breaking existing functionality and does not change the logical purpose of the module. 

### How else could you use this CRUD Python module in the future? What were the advantages of working in this way?
Using the Python module for Create, Read, Update, and Delete (CRUD) organized all the database functionality into a reusable module. That module could be used by other projects to work with the same database. For example, a command line program could be written for extract, transform, and load (ETL) purposes. Or another web page written to provide a different view of the data for reporting purposes. 

### How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

I approach a problem with an idea on how I think the end user will interact with the requested feature. Not all problems have an external end user or customer, even internal use applications have a user even if it's the programmer themself. In this assignment, the various components were given and all I had to do was integrate them. The database and data were given. I had to load and setup access control. The Dash API and MongoDB driver were given, and I had to add functionality to integrate them into an HTML output. In future work, unless the customer has an existing data source, database design will have to be included in the project scope.

### What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists engineer solutions to answer questions. In this project, the questions were what animals are available that are suitable for a given rescue program and where are they located. A company like Grazioso Salvare could use the information to expand their business to other cities besides Austin Texas but partnering with the shelters there and loading the data and using it to begin new training programs. They may also expand to other trainings and using the existing data to find new breeds suitable for those new initiatives.
