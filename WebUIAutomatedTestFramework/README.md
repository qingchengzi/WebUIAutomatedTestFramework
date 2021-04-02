
Python3+unittest+HTMLTestRunner+apscheduler实现web端ui自动化测试;

    采用分层设计思想,Page object设计模式,使用apscheduler来完成定时任务,具体测试中需要的参数通过数据驱动的方式进行存储和读取。 将页面元素定位于元素操作进行分层，将谷歌浏览器实例化后driver对象常用属性和方法全部封装到base.py中，页面元素定位通过继承base.py中的BasePage来实现元素的操作。 用例执行成功或者失败后自动截图功能，运行失败后生成对应的日志。 通过修改配置文件可以实现有头还是无头浏览器来运行自动化测试用例。 通过定时任务执行完用例后，已附件的形式将测试报告发送到指定的邮箱。

框架目录简介

config --->settings.py 框架中常量的配置，例如：是否使用无头浏览器运行、邮箱配置、目录路径的配置等。 

database --->数据驱动，可将数据存放在text、json、excel、数据库中通过unittest来读取存在在这里的数据。

debugcode --->调试代码用 logs --->日志目录，用例执行失败时生成记录。

page --->page层针对每个待操作的元素进行封装，然后再到具体的测试用例中进行引用。 根据具体业务可以将一个页面或者几个页面创建一个page对象。 base.py中封装了浏览器对象driver操作元素的常用属性和方法， 每个页面的page类通过继承的方式来调用base.py中的方法和属性，当页面元素变化时，只需要维护page层的元素定位即可。

screenshot --->用例运行时以年月日这种方式生成一级目录，自动生成两个二级目录：errorsdir目录、success目录。 
errorsdir目录:用来保存用例执行失败是页面的错误截图； success目录:用来保存用例执行成功后的页面截图； 默认只保留最近10天的截图，超过10天的截图自动会删除，可以通过配置文件修改天数。
针对具体测试用例中需要测试数据，使用了数据驱动设计方法，具体做法通过在database存放数据，支持数据格式.json,text,excel登录， 登录测试用例中使用了DDT进行参数化。 testreport --->以年月日时分秒_rest.html方式生成html格式的测试报告，该测试报告中包含了错误截图功能，优化为中文显示。 默认只保留最近10份测试报告，超过10份自动会删除，可以通过配置文件修改份数。

testsuite --->测试用例目录，里面的py文件必须以_test.py结尾，测试文件的执行顺序根据ASCII码顺序执行； 例子：a_login_test.py 优先 b_add_housing_test.py执行 a_login_test.py：作者在工作中使用的登录测试用例，类setUpClass中实例化page目录中的LoginPage()类来完成页面元素定位和操作，然后返回值进行断言。测试用例2使用的ddt方式将不同的测试数据来运行测试用例。 b_b_add_housing_test.py：作者在工作中使用的添加房源用例，里面使用了模块级别Fixture，因为作者在工作中该py文件中定义了几个类，使用通过模块级别的setUpModule 和 tearDownModule来进行初始化和结束后的一些操作。 b_b_add_housing_test.py具体用例通过初始化后获取到的HousingPage类对象，进行元素的定位、操作返回值，然后断言。 

util --->工具包 common_moduel.py中实现了截图、读取数据、删除目录的功能，测试用例中通过实例化该类进行调用。 

LogHandler.py 日志写入功能 oracle_job.py 实现定时任务 

send_email.py 发送邮件 

main_run.py 整个框架的执行入口，通过unittest.defaultTestLoader.discover("./testsuite", pattern="*_test.py")的设置来执行testsuite目录下面所有已_test.py结尾的文件。
