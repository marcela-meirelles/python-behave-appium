INSTALLATION:

pip install -r requirements.txt

Execute:

python run_tests.py


Sometimes force reinstall is required for appium-python-client:

pip install --force-reinstall "Appium-Python-Client<4.0.0"


Add this to take screenshots:
allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

Use this to create report:
behave -f allure_behave.formatter:AllureFormatter -o "allure_report" create_account.feature

behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
This will generate JSON report to %allure_result_folder%. Then, to view HTML report you can use Allure Command line (plugins for Jenkins/TeamCity/Bamboo also available)

$ allure serve %allure_result_folder%
