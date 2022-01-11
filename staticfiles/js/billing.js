function populate(s1,s2)
{
  var s1=document.getElementById(s1);
  var s2=document.getElementById(s2);
  s2.innerHTML="";
  if(s1.value=="india")
  {
    var optionArray=['karnataka|Karnataka','kerala|Kerala','maharashtra|Maharashtra'];
  }
  else if(s1.value=='usa')
  {
    var optionArray=['texas|Texas','california|California'];
  }
  for(var option in optionArray)
  {
    var pair=optionArray[option].split("|");
    var newoption=document.createElement("option");
    newoption.value=pair[0];
    newoption.innerHTML=pair[1];
    s2.options.add(newoption);
  }
}
function country_code(){
  var val = document.getElementById("slct1").value;
  if(val==="india"){
    document.getElementById("phone").value="(+91)";
  }
  else if(val==="usa"){
    document.getElementById("phone").value="(+1)";
  }

}
