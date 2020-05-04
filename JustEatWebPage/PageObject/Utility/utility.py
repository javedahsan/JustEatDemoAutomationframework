class Utility:

    # def findById
    def findById(self,objParm):
        result = self.find_element_by_id(objParm)
        return result

    # def findByClass
    def findByClass(self,objParm):
        result = self.driver.find_element_by_class(objParm)
        return result

    # def findByName
    def findByName(self,objParm):
        result = self.driver.find_element_by_name(objParm)
        return result

    def findByCss(self,objParm):
        result = self.driver.find_element_by_css_selector(objParm)
        return result

    # def findByXpath
    def findByXpath(self,objParm):
        result = self.driver.find_element_by_xpath(objParm)
        return result

    # def find by partial Link
    def findByPartialLink(self,objParm):
        result = self.driver.find_element_by_partial_link_text(objParm)
        return result