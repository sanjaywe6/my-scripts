import webbrowser
import urllib.parse
import time

def open_google_dorks(target):

    for dork in fileTypesSearch:
        query = f"site:{target} {dork}"
        encoded_query = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open_new_tab(url)
        time.sleep(1)  # delay to avoid browser overload

if __name__ == "__main__":
    typeList = ['SECRETS / CONFIG / CREDENTIAL LEAKS',
                'SOURCE CODE / FRONTEND FILES',
                'DATA DUMPS / EXPORTS',
                'LOGS / DEBUG / ERROR FILES',
                'DOCUMENTATION / INTERNAL NOTES',
                'BACKUPS / OLD FILES',
                'DEVOPS / INFRASTRUCTURE FILES',
                'API SPECIFICATIONS / DOCS',
                'NEXT.JS SPECIFIC FILES',
                'CLOUD STORAGE / BUCKETS',
                'ARCHIVE FILES',
                'MEDIA FILES',
                'ADMIN / LOGIN PAGES'
                ]
    fileTypes = [

        # SECRETS / CONFIG / CREDENTIAL LEAKS (TOP PRIORITY)
        [
            "ext:env", "ext:env.local", "ext:env.dev", "ext:env.prod", "ext:env.production","ext:ini", "ext:conf", "ext:config", "ext:properties", "ext:toml","ext:json", "ext:yaml","ext:yml","inurl:config", "inurl:settings", "inurl:credentials", "inurl:secrets","filetype:env", "filetype:ini", "filetype:conf", "filetype:json","ext:graphql"
        ],

        # SOURCE CODE / FRONTEND FILES
        [
            "ext:js", "ext:map","ext:ts", "ext:tsx", "ext:jsx","filetype:js", "filetype:map"
        ],

        # DATA DUMPS / EXPORTS (IDOR GOLD)
        [
            "ext:csv", "ext:tsv","ext:xls", "ext:xlsx","ext:xml", "ext:json", "ext:pdf","filetype:csv", "filetype:xlsx", "filetype:pdf"
        ],

        # LOGS / DEBUG / ERROR FILES
        [
            "ext:log", "ext:logs","ext:trace", "ext:stacktrace","ext:error", "ext:debug","ext:out", "ext:dump","inurl:debug", "inurl:error", "inurl:trace"
        ],

        # DOCUMENTATION / INTERNAL NOTES
        [
            "ext:txt", "ext:md", "ext:rst","ext:doc", "ext:docx","ext:ppt", "ext:pptx","ext:pdf","inurl:readme", "inurl:changelog", "inurl:todo", "inurl:notes","filetype:md", "filetype:txt"
        ],

        # BACKUPS / OLD FILES (CLASSIC MISTAKES)
        [
            "ext:bak", "ext:backup", "ext:old", "ext:orig","ext:copy", "ext:tmp", "ext:temp", "ext:swp","inurl:backup", "inurl:old", "inurl:temp"
        ],

        # DEVOPS / INFRASTRUCTURE FILES ( HIGH IMPACT)
        [
            "inurl:.git", "ext:gitignore","inurl:gitlab", "inurl:github","dockerfile", "docker-compose","ext:tf", "ext:tfvars","inurl:k8s", "inurl:kube","inurl:terraform", "inurl:ansible"
        ],

        # API SPECIFICATIONS / DOCS
        [
            "inurl:api", "inurl:internal", "inurl:private","inurl:swagger", "inurl:openapi","ext:json", "ext:yaml", "ext:yml","ext:graphql", "ext:gql","ext:proto", "ext:wsdl", "ext:raml"
        ],

        # NEXT.JS SPECIFIC FILES (VERY IMPORTANT)
        [
            "inurl:_next","inurl:_next/static","inurl:_next/data","ext:json","inurl:routes-manifest.json","inurl:build-manifest.json","inurl:prerender-manifest.json","inurl:middleware-manifest.json"
        ],

        # CLOUD STORAGE / BUCKETS
        [
            "inurl:s3", "inurl:bucket","inurl:storage", "inurl:blob","inurl:cdn","inurl:uploads", "inurl:files", "inurl:media","inurl:backup"
        ],

        # ARCHIVE FILES
        [
            "ext:zip", "ext:rar", "ext:7z","ext:tar", "ext:gz", "ext:tgz", "ext:bz2","filetype:zip", "filetype:tar"
        ],

        # MEDIA FILES (LOW PRIORITY – usually skip)
        [
            "ext:jpg", "ext:png", "ext:svg", "ext:gif","ext:mp4", "ext:mp3","ext:woff", "ext:woff2","ext:css","inurl:admin","inurl:administrator","inurl:login","inurl:auth","inurl:oauth","inurl:sso","inurl:internal","inurl:private","inurl:staff","inurl:dashboard","inurl:manage","inurl:console","inurl:signup","inurl:register","inurl:reset","inurl:forgot","inurl:password","inurl:verify","inurl:otp","inurl:2fa","inurl:mfa","inurl:session","inurl:token","inurl:user","inurl:users","inurl:profile","inurl:account","inurl:settings","inurl:role","inurl:roles","inurl:permission","inurl:permissions","inurl:payment","inurl:checkout","inurl:order","inurl:invoice","inurl:billing","inurl:subscription","inurl:pricing","inurl:plan","inurl:refund","inurl:search","inurl:filter","inurl:query","inurl:export","inurl:download","inurl:report","inurl:upload","inurl:import","inurl:file","inurl:attachment","inurl:media","inurl:avatar","inurl:image","inurl:document","inurl:dev","inurl:test","inurl:staging","inurl:stage","inurl:uat","inurl:beta","inurl:sandbox","inurl:demo","inurl:qa","inurl:status","inurl:health","inurl:metrics","inurl:actuator","inurl:monitor","inurl:ping","inurl:alive","inurl:ready","inurl:webhook","inurl:callback","inurl:integration","inurl:hook","inurl:listener","inurl:notify","inurl:cms","inurl:panel","inurl:backend","inurl:control","inurl:manager","inurl:moderator","inurl:editor"
        ]

    ]

    target = input("Enter target domain (example: example.com): ")
    print("Choose file type category to search for: \n")
    for index, fileType in enumerate(typeList, start=1):
        print(f"{index}. {fileType}")
    choice = int(input("\nEnter the number corresponding to your choice: ")) - 1
    print(f"\nSearching for {typeList[choice]} files on {target}...\n")
    print("Opening Google search tabs for filetype...\n")

    fileTypesSearch = fileTypes[choice]
    open_google_dorks(target)
