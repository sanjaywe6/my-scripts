import webbrowser
import urllib.parse
import time

def open_google_dorks(target):

    for dork in fileTypesSearch:
        query = f"site:{target} {dork}"
        encoded_query = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"

        print(f"Opening: {query}")
        webbrowser.open_new_tab(url)

        # Increased delay to reduce CAPTCHA chances
        time.sleep(3)

if __name__ == "__main__":

    typeList = [
        'SECRETS / CONFIG / CREDENTIAL LEAKS',
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

        # Split old 12 into two parts
        'MEDIA FILES (PART A)',
        'MEDIA FILES (PART B)',

        # Proper 14th category
        'ADMIN / LOGIN PAGES'
    ]

    fileTypes = [

        # 1 - SECRETS / CONFIG / CREDENTIAL LEAKS
        [
            "ext:env", "ext:env.local", "ext:env.dev",
            "ext:env.prod", "ext:env.production",
            "ext:ini", "ext:conf", "ext:config",
            "ext:properties", "ext:toml",
            "ext:json", "ext:yaml", "ext:yml",
            "inurl:config", "inurl:settings",
            "inurl:credentials", "inurl:secrets",
            "filetype:env", "filetype:ini",
            "filetype:conf", "filetype:json",
            "ext:graphql"
        ],

        # 2 - SOURCE CODE
        [
            "ext:js", "ext:map",
            "ext:ts", "ext:tsx", "ext:jsx",
            "filetype:js", "filetype:map"
        ],

        # 3 - DATA DUMPS
        [
            "ext:csv", "ext:tsv",
            "ext:xls", "ext:xlsx",
            "ext:xml", "ext:json",
            "ext:pdf",
            "filetype:csv",
            "filetype:xlsx",
            "filetype:pdf"
        ],

        # 4 - LOGS
        [
            "ext:log", "ext:logs",
            "ext:trace", "ext:stacktrace",
            "ext:error", "ext:debug",
            "ext:out", "ext:dump",
            "inurl:debug",
            "inurl:error",
            "inurl:trace"
        ],

        # 5 - DOCUMENTATION
        [
            "ext:txt", "ext:md", "ext:rst",
            "ext:doc", "ext:docx",
            "ext:ppt", "ext:pptx",
            "ext:pdf",
            "inurl:readme",
            "inurl:changelog",
            "inurl:todo",
            "inurl:notes",
            "filetype:md",
            "filetype:txt"
        ],

        # 6 - BACKUPS
        [
            "ext:bak", "ext:backup",
            "ext:old", "ext:orig",
            "ext:copy", "ext:tmp",
            "ext:temp", "ext:swp",
            "inurl:backup",
            "inurl:old",
            "inurl:temp"
        ],

        # 7 - DEVOPS
        [
            "inurl:.git",
            "ext:gitignore",
            "inurl:gitlab",
            "inurl:github",
            "dockerfile",
            "docker-compose",
            "ext:tf",
            "ext:tfvars",
            "inurl:k8s",
            "inurl:kube",
            "inurl:terraform",
            "inurl:ansible"
        ],

        # 8 - API
        [
            "inurl:api",
            "inurl:internal",
            "inurl:private",
            "inurl:swagger",
            "inurl:openapi",
            "ext:json",
            "ext:yaml",
            "ext:yml",
            "ext:graphql",
            "ext:gql",
            "ext:proto",
            "ext:wsdl",
            "ext:raml"
        ],

        # 9 - NEXT.JS
        [
            "inurl:_next",
            "inurl:_next/static",
            "inurl:_next/data",
            "ext:json",
            "inurl:routes-manifest.json",
            "inurl:build-manifest.json",
            "inurl:prerender-manifest.json",
            "inurl:middleware-manifest.json"
        ],

        # 10 - CLOUD STORAGE
        [
            "inurl:s3",
            "inurl:bucket",
            "inurl:storage",
            "inurl:blob",
            "inurl:cdn",
            "inurl:uploads",
            "inurl:files",
            "inurl:media",
            "inurl:backup"
        ],

        # 11 - ARCHIVES
        [
            "ext:zip", "ext:rar",
            "ext:7z", "ext:tar",
            "ext:gz", "ext:tgz",
            "ext:bz2",
            "filetype:zip",
            "filetype:tar"
        ],

        # 12A - MEDIA
        [
            "ext:jpg",
            "ext:png",
            "ext:svg",
            "ext:gif",
            "ext:mp4",
            "ext:mp3",
            "ext:woff",
            "ext:woff2",
            "ext:css"
        ],

        # 12B - EXTRA RECON DORKS
        [
            "inurl:dev",
            "inurl:test",
            "inurl:staging",
            "inurl:beta",
            "inurl:sandbox",
            "inurl:demo",
            "inurl:qa",
            "inurl:status",
            "inurl:health",
            "inurl:metrics",
            "inurl:webhook",
            "inurl:callback",
            "inurl:integration"
        ],

        # 13 - ADMIN / LOGIN PAGES
        [
            "inurl:admin",
            "inurl:administrator",
            "inurl:login",
            "inurl:auth",
            "inurl:oauth",
            "inurl:sso",
            "inurl:dashboard",
            "inurl:console",
            "inurl:panel",
            "inurl:backend",
            "inurl:manage",
            "inurl:cms",
            "inurl:staff",
            "inurl:internal",
            "inurl:private"
        ]
    ]

    target = input("Enter target domain (example: example.com): ")

    print("\nChoose file type category:\n")

    for index, fileType in enumerate(typeList, start=1):
        print(f"{index}. {fileType}")

    choice = int(input("\nEnter choice number: ")) - 1

    if choice < 0 or choice >= len(fileTypes):
        print("Invalid choice.")
        exit()

    print(f"\nSearching for {typeList[choice]} on {target}...\n")

    fileTypesSearch = fileTypes[choice]

    open_google_dorks(target)