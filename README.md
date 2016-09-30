We are using the Django REST framework.

Why ?

It's pretty much all we should need. Except for the server which we use to deploy it. For that we should probably use Apache, but we can figure that part out later.

Read this article to sorta figure out what this framework is about:

http://ngenworks.com/technology/how-django-rest-framework-changed-my-life/

Then read these tutorials:

http://www.django-rest-framework.org/tutorial/1-serialization/

http://www.django-rest-framework.org/tutorial/2-requests-and-responses/

http://www.django-rest-framework.org/tutorial/3-class-based-views/

http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/

Then read the quickstart in the beginning. And try to implement the generic app there.

Also,

Here's some of the things it's important you understand to be able to grasp anything that's happening tomorrow:

a) What "querying an endpoint" means: You query an HTML "endpoint" with a certain "HTTP method" and use it to either receive/send JSONs based on the method you used. The two popular methods (and possibly the only methods we need to know about tomorrow) are GET and POST.

You can use the methods GET and POST with pretty much any service. For example, you can use your command line and use the "curl" utility to use them. An "endpoint" is simply a web address, it's a component of HTTP which instead of offering you browsers offers you a service. Even if you access the "Endpoint" with your browser you will perform a HTTP method on it. So for GET we can literally type the url into our browser. But we'll use a specialised application for these methods first which makes it very use to use the methods: Postman. 

Install it as a chrome extension here:

https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop

But what we need to do eventually: is to automate these HTTP methods. So we need to build an application to automate these methods, then possibly make a database into which we push and load information from. We can probably use MySQL to do that. 

So what we essentially need to split the work into:

a)Front-end
b)Back-end

So 2 people each probably, but for us to work together we need to know what everyone else is doing, otherwise it's impossible to build parts that fit together.

 We're using Django REST Frameworks as the glue that will hold everything together, we can create the front-end and back-end both insides this.

 Read up on "Models", "Views" and "Controllers", understand how the three work together.

