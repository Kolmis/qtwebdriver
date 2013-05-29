import subprocess as sp

filename = "./src/wdversion.cc"
p = sp.Popen(["git", "describe" , "--abbrev=10", "--dirty", "--always"], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)

data = p.stdout.readline()

versionfile = open (filename, 'w')
versionfile.write("namespace webdriver {\n")
versionfile.write("extern const char kProductName[] = \"WebDriver-cisco-cmt\";\n")
versionfile.write("extern const char kVersionNumber[] = \"0.2.0\";\n")
versionfile.write("extern const char kBuildTime[] = __TIME__;\n")
versionfile.write("extern const char kBuildDate[] = __DATE__;\n")
versionfile.write("extern const char kLastChanges[] = \"" + data.strip() + "\";\n")
versionfile.write("}")
versionfile.close()

p.stdout.close()
p.stdin.close()