<script>
  var data;
  var div_id;
  var text_id;
  var chart_id;
  var function_type;

  function communication(){
    var httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
      alert('Abandon :( Impossible de créer une instance de XMLHTTP');
      return false;
    }
    
    httpRequest.onload = function_type;

    httpRequest.open('POST', 'test_POST.php');  
    httpRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    httpRequest.send(data);
  }  
</script>

<script>
  function update_text(){
      document.getElementById(text_id).innerHTML = this.responseText;
  }
  
  function update_information(){
    none;
    //TODO
  }


  function update_chart(){
    none;
    //TODO
  }

  function update_all(){
    update_text();
    update_chart();
  }
</script>
