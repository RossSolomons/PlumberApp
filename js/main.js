(function () {
  var form = document.querySelector("#touch-form");
  if (!form) return;

  var preview = document.querySelector("#message-preview");
  var status = document.querySelector("#form-status");

  function field(name) {
    var value = new FormData(form).get(name);
    return value ? String(value).trim() : "";
  }

  function buildMessage() {
    var name = field("name");
    var phone = field("phone");
    var service = field("service");
    var message = field("message");
    var lines = ["Hi D&A Plumbing,"];

    if (name) lines.push("", "My name is " + name + ".");
    if (service) lines.push("I need help with " + service.toLowerCase() + ".");
    if (phone) lines.push("You can reach me on " + phone + ".");
    if (message) lines.push("", message);

    return lines.join("\n");
  }

  function whatsAppUrl() {
    var cell = field("cell") || "27743583766";
    return "https://wa.me/" + cell + "?text=" + encodeURIComponent(buildMessage());
  }

  function showPreview() {
    if (!preview) return;
    var name = field("name");
    var service = field("service");
    var message = field("message");
    preview.textContent =
      name || service || message
        ? buildMessage()
        : "Your message will show here as you type.";
  }

  function setStatus(opened, url) {
    if (!status) return;
    status.replaceChildren();
    if (opened) {
      status.textContent = "WhatsApp should be open with your message ready to send.";
      return;
    }
    status.append("The new tab was blocked. ");
    var link = document.createElement("a");
    link.href = url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.textContent = "Open WhatsApp";
    status.append(link, " to send it.");
  }

  form.addEventListener("input", showPreview);
  form.addEventListener("change", showPreview);

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (!form.reportValidity()) return;
    var url = whatsAppUrl();
    var opened = window.open(url, "_blank", "noopener,noreferrer");
    setStatus(Boolean(opened), url);
  });

  showPreview();
})();
