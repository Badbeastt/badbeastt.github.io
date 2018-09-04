import cgi

def htmlTop():
    print("""Content-type:text/html\n\n
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <title>Answers</title>
            </head>
            <body>""")

def htmlTail():
    print("""</body>
        </html>""")

def getData(num):
    formData = cgi.FieldStorage()
    ans = formData.getvalue('ans_'+str(num));
    return ans

#main program
if __name__ == "__main__":
    try:
        htmlTop()
        ans_list = []
        for x in range(253, 318):
            ans_list.append(getData(x))
        print("The answers are:\n{0}".format(ans_list))
        htmlTail()
    except:
        cgi.print_exception()
    
    #for x in range(0,len(ans_list))
        #browser.find_elements_by_css("input[type='radio'][value='%s']".format(ans_list[x])).click
