<input type="text" name="name" id="id_name" data-captalize>

$('input').filter('[data-captalize]').keyup(function(k){
  var split = this.value.split(' ');
  var p = ["da", "de", "di", "do", "du"]
      for (var i = 0, len = split.length; i < len; i++) {
          split[i] = split[i].charAt(0).toUpperCase() + split[i].slice(1).toLowerCase();
      }
      this.value = split.join(' ');
});
