node {
    stage('Git Clone') {
        git branch: '${branch}', credentialsId: '1b00358b-6ad1-4902-b58d-aaef42619cd9', url: 'https://github.com/half-tested/playwright-python.git'
    }
    stage('Setup Envoronment') {
        sh """
        python3 -m venv venv
        source venv/bin/activate
        pip3 install -r requirements.txt
        playwright install
        """
    }
    stage('Execute Tests') {
        catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
            sh """
            pytest --alluredir=allure --clean-alluredir --allure-features=custom --screenshot=${screenshot} --video=${video} --junit-xml=junit.xml
            """
        }
    }
    stage('Generate Report') {
        junit 'junit.xml'

        def envFileContent = """
        branch=${branch}
        other=value
        """
        writeFile file: 'allure/environment.properties', text: "${envFileContent}"
        allure([
            includeProperties: true,
            jdk: '',
            properties: [[key: 'allure.issues.tracker.pattern', value: 'http://tracker.company.com/%s']],
            reportBuildPolicy: 'ALWAYS',
            results: [[path: 'allure']]
        ])
    }
}