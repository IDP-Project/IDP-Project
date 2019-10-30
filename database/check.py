
import psycopg2

def main():

	connection = psycopg2.connect("dbname='restore' user='postgres' host='localhost' password='test123'") #database connection
	version = contents = ' ' 
	vFile = open("version.txt","r")   #opening file containing version and vendor name which are fetched after scanning the linux system
	if vFile.mode == "r":
		contents = vFile.read()
		split_contents = contents.split("\n") #after reading the file, split each string/word
		vendor = split_contents[0]
		vers = split_contents[1]
	cursor = connection.cursor()  
	cursor.execute("""SELECT cve_items_cve_affects_vendor_vendor_data_vendor_name,cve_items_cve_affects_vendor_vendor_data_product_product_data_v from database""") #command to get vendor name and version 

	rows = cursor.fetchall()  #fetching all vendorname and version from the database and store it in "rows" variable
	for rr in rows:
		r1 = rr[0]
		r2 = rr[1]
	
		if rr[0] == vendor and rr[1] == vers: #comparing vendor name and version between database value and version text file.
			cursor.execute("SELECT * from database where cve_items_cve_affects_vendor_vendor_data_vendor_name = '%s'"%r1 +" and cve_items_cve_affects_vendor_vendor_data_product_product_data_v = '%s';"%r2) #after comparing, fetch whole row from database which has other information.
			r = cursor.fetchall() #fetch whole row and store it into "r" variable.
			for content in r: 		#loop is used for printing/showing whole information.
				print "------------------------------------------------------------------------------------------------------"
				print "The vulnerability detail for version: ",vers + " and vendor: ",vendor
				print "\n"	
				print "Description: ", content[6]
				print "\n"	
				print "Published date: ", content[20]
				print "Modified date: ", content[21]
				print "\n"
								
				print "CVE ID: ", content[0]
				print "Vender name: ", content[1]
				print "Product name: ", content[2]
				print "Version: ", content[3]
				print "CWE Id: ", content[4]

				print "\nCVSS v2.0 Severity and Metrics: \n"
				print "Vector: ", content[9]
				print "Access Vector: ", content[10]
				print "Access Complexity: ", content[11]
				print "Authentication(A): ", content[12]
				print "Confidentiality impact: ", content[13]
				print "Integrity impact: ", content[14]
				print "Availability impact: ", content[15]
				print "Base score: ", content[16]
				print "Severity: ", content[17]
				print "Exploitability score: ",content[18]
				print "Impact score: ", content[19]
				
				
				print "\nCVSS v3.0 Severity and Metrics:\n"
				print "Vector String: ", content[23]
				print "Attack vector: ", content[24]
				print "Attack complexity: ", content[25]
				print "Privileges required: ", content[26]
				print "User interaction: ", content[27]
				print "Scope: ", content[28]
				print "Confidentiality impact: ", content[29]
				print "Integrity impact: ", content[30]
				print "Availability impact: ", content[31]
				print "Base Score: ", content[32]
				print "Base Severity: ", content[33]
				print "Exploitability score: ", content[34]
				print "Impact Score: ", content[35]
				print "\n"
				print "Mitigation reference url: ", content[5]
				print "Configurations cpe match: ", content[7]

					
		

if __name__ == "__main__":		#main function to run the program
	main()
