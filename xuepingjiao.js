//女票学评教一键刷脚本
var table = window.frames["zhuti"].document.getElementById("DataGrid1");
  console.log(table);
  var body = table.children;
  var trs = body[0].children;
  for (let i = 1; i < 11; i++) {
      var tds = trs[i].getElementsByTagName("td");
      for (let j = 3; j < tds.length; j++) {
        var select = tds[j].firstElementChild;
        var option_good = select.children[1];
        option_good.selected = "selected";
      }
  }

