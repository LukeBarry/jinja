from flask import Flask, render_template
app = Flask(__name__)
import datetime

# Using the @app.template_filter() decorator you are registering the datetimefilter() function as a filter.
# The default name for the filter is just the name of the function; however, 
# you can customize it by passing in an argument to the function – e.g, @app.template_filter("formatdate")
# Next, you are adding the filter to the Jinja environment, making it accessible. Now it’s ready to use.  I added the <h4> tag to the template.html file
@ app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(format)

# Here you are establishing the route / , which renders the template template.html via the function render_template()
#This function must have a template name. Optionally, you can pass in arguments to the template, like in the example – my_string and my_list.
@app.route("/")
def template_test():
    return render_template('template.html', 
                            my_string="Wheeeee!",
                            my_list=[0,1,2,3,4,5],
                            current_time=datetime.datetime.now())

# Finally, in run.py pass in the datetime to your template along with my_list and my_string 
# (remembering to import the datetime module at the top of the file                           
@app.route("/home")                 
def home():
    return render_template('template.html',
                            my_string="I'm the home page",
                            my_list=[0,1,2,3,4,5],
                            current_time=datetime.datetime.now())
                            
@app.route("/about")
def about():
    return render_template('template.html',
                            my_string="I'm the about page",
                            my_list=[0,1,2,3,4,5],
                            current_time=datetime.datetime.now())

@ app.route("/contact")
def contact():
    return render_template('template.html',
                            my_string="I'm the contact page",
                            my_list=[0,1,2,3,4,5],
                            current_time=datetime.datetime.now())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
    
    





