var React = require('react');


export default class Python extends React.Component {
    //TODO DOWNLOAD
    constructor(props) {
        super(props);
        this.state = {
            filename:"myBlocklyCode.py",
            data:""
        };

        this.handleInputChange = this.handleInputChange.bind(this);
        this.download = this.download.bind(this);
        this.upload = this.upload.bind(this);
        this.send = this.send.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
        if (name=="data") {document.getElementById("data").value = this.state.data;}
    }

    download(event){
        /* DOWNLOAD FUNCTION
          Allows users to download raw code as a file. Users must
          manually input file name and file ext. */
        console.log("download listener");
        event.preventDefault();
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(this.state.data));
        element.setAttribute('download', this.state.filename);
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }

    //TODO
    upload(event){
        console.log("upload listener");
        var files = event.target.files;
        var reader = new FileReader();
        var f = files[0];
        // reader.onload = (function(this.state.file) {
        //     return function(e) {
        //         this.state.code = e.target.result;
        //     }
        // })(f);
        // reader.readAsText(f);
    }

    send(){
        console.log("send listener");
        $.ajax({
            method: "POST",
            url: '/uploadScript',
            dataType: 'json',
            data: JSON.stringify({
                name: $("#id").val(),
                script: getBlocklyScript()
            }),
            contentType: 'application/json'
        });
    }

    render(){
        return (
            <div id ="python" className ="box">
                Python
                File Name: <input type="text" name="filename" value={this.state.filename} onChange={this.handleInputChange}/><br/>
                <textarea name="data" id="data" value={this.state.data} onChange={this.handleInputChange}></textarea><br/>
                <button id="submit" onClick={this.download}>Download</button>
                <button id="send" onClick={this.send}>Run Code</button>
                <form>
                    <input
                        type="file"
                        id="upload"
                        multiplesize="1"
                        accept=".py"
                    />
                </form>
            </div>
        )
    }
}
