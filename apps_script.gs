// Afritech Sports website: saves each "Tell us who you are" answer to the private visitors Sheet.
// Setup: in the Sheet, Extensions > Apps Script, replace everything with this file, Save,
// then Deploy > New deployment > Web app, Execute as: Me, Who has access: Anyone > Deploy.
// Copy the Web app URL (ends in /exec) and send it to Claude.
var SHEET_ID = '1PmBSBd0Iu6Yo_VGSMUAgmdWXvTyjm6NTXUlBCRC-Qxs';
var FIELDS = ['type', 'team', 'level', 'country', 'city', 'org', 'topic', 'page', 'lang', 'src', 'consent'];

function clean_(v) {
  v = String(v || '').slice(0, 200);
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function doPost(e) {
  var p = (e && e.parameter) || {};
  if (p.consent !== 'yes') return ContentService.createTextOutput('no consent');
  var row = [new Date()];
  for (var i = 0; i < FIELDS.length; i++) row.push(clean_(p[FIELDS[i]]));
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try { SpreadsheetApp.openById(SHEET_ID).getSheets()[0].appendRow(row); }
  finally { lock.releaseLock(); }
  return ContentService.createTextOutput('ok');
}
