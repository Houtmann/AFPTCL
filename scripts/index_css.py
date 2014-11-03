"""Create a index.css file, for design the html report"""


def index_css():
    index_css = open('index.css', 'a')
    index_css.write("""body {margin: 0px; padding: 0px; background: #FFFFFF; font: 13px/20px Arial, Helvetica, sans-serif; color: #535353;}
#content {padding: 30px;}
#header {width:100%; padding: 10px; line-height: 25px; background: #07A; color: #FFF; font-size: 20px;}
h1 {font-size: 20px; font-weight: normal; color: #07A; padding: 0 0 7px 0; margin-top: 25px; border-bottom: 1px solid #D6D6D6;}
h2 {font-size: 20px; font-weight: bolder; color: #07A;}
h3 {font-size: 16px; color: #07A;}
h4 {background: #07A; color: #FFF; font-size: 16px; margin: 0 0 0 25px; padding: 0; padding-left: 15px;}
ul.nav {list-style-type: none; line-height: 35px; padding: 0px; margin-left: 15px;}
ul li a {font-size: 14px; color: #444; text-decoration: none; padding-left: 25px;}
ul li a:hover {text-decoration: underline;}
p {margin: 0 0 20px 0;}
table {max-width: 100%; min-width: 700px; padding: 0; margin: 0; border-collapse: collapse; border-bottom: 2px solid #e5e5e5;}
.keyword_list table {width: 100%; margin: 0 0 25px 25px; border-bottom: 2px solid #dedede;}
table th {display: table-cell; text-align: left; padding: 8px 16px; background: #e5e5e5; color: #777; font-size: 11px; text-shadow: #e9f9fd 0 1px 0; border-top: 1px solid #dedede; border-bottom: 2px solid #e5e5e5;}
table td {display: table-cell; padding: 8px 16px; font: 13px/20px Arial, Helvetica, sans-serif; max-width: 500px; min-width: 125px; word-break: break-all; overflow: auto;}
table tr:nth-child(even) td {background: #f3f3f3;}""")
    index_css.close()
