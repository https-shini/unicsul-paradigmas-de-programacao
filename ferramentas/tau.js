// Executa um programa Prolog com Tau-Prolog: node tau.js arquivo.pl "consulta."
const pl = require("tau-prolog"); require("tau-prolog/modules/lists")(pl);
const fs = require("fs");
const prog = fs.readFileSync(process.argv[2], "utf8").replace(/^:-\s*initialization\(main\)\.\s*$/m, "");
const goal = process.argv[3] || "main.";
const session = pl.create(100000);
let out = ""; session.standard_output = { put: (t)=>{ out += t; return true; }, flush: ()=>true };
session.consult(prog, { success: () => {
  session.query(goal, { success: () => {
    const next = () => session.answer({ success: a => { out += "\n" + session.format_answer(a); next(); },
                                         fail: () => { out += "\nfalse."; done(); }, error: e => { out += "\nERR " + pl.format_answer(e); done(); }, limit: () => done() });
    next();
  }, error: e => { console.log("QUERY ERR", pl.format_answer(e)); } });
}, error: e => { console.log("CONSULT ERR", pl.format_answer(e)); } });
function done(){ process.stdout.write(out + "\n"); }
