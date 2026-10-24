import json, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for d in ["Task2/data","Task2/app","Task2/calculations","Task2/evidence","Task2/capstone","task1"]:
    os.makedirs(f"{R}/{d}", exist_ok=True)

# (sem, code, title, L,T,P, C, status, newC, reasons)   -- official columns copied from the program-structure page
K,U,Rd,A = "KEEP","UPDATE","REDUCE","ADD"
rows = [
("I","EG101","English Language Skills",2,0,2,3,K,3,[]),
("I","ES101","Engineering Graphics",1,0,4,3,K,3,[]),
("I","BS101","Chemistry",2,1,2,4,K,4,["R9"]),
("I","HS101","Understanding India",0,0,0,0,K,0,["R9"]),
("I","BS102","Physics",2,1,2,4,K,4,["R9"]),
("I","BS103","Linear Algebra and Ordinary Differential Equations",2,1,0,3,K,3,["R9"]),
("I","ES105","Computer Programming",2,0,4,4,K,4,["R5","R6"]),
("II","EG102","Professional Communication",2,1,0,3,K,3,["R9"]),
("II","ES102","Digital Fabrication",1,1,2,3,Rd,2,["R8"]),
("II","ES103","Environmental Sciences",2,0,0,2,K,2,["R9"]),
("II","ES104","Basic Electronics",2,1,2,4,K,4,[]),
("II","BS104","Higher Calculus",2,1,0,3,K,3,["R9"]),
("II","ES106","Data Structures",2,0,4,4,K,4,["R5","R6"]),
("II","ES107","Introduction to DS and AI",2,1,0,3,K,3,[]),
("II","ADD-01","API Design, Integration and Python Automation (proposed)",2,0,2,0,A,3,["R1","R5","R10"]),
("III","MG201","Engineering Economics and Management",2,1,0,3,K,3,[]),
("III","BS105","Probability & Statistics",2,1,0,3,K,3,["R9"]),
("III","ES201","Object Oriented Programming Concepts",2,0,4,4,K,4,["R5"]),
("III","CR201","Power Skills - I",0,0,2,1,K,1,["R9"]),
("III","DS201","Introduction to IoT",2,0,2,3,Rd,2,["R8"]),
("III","DS202","Database Management Systems",2,1,2,4,U,4,["R1","R4","R6"]),
("III","DS203","Artificial Intelligence",3,0,0,3,K,3,[]),
("III","DS205","Operating Systems",3,0,2,4,K,4,["R6"]),
("IV","Not listed","Digital Humanities Elective (code not specified on page)",3,0,0,3,K,3,[]),
("IV","CR202","Power Skills - II",0,0,2,1,K,1,["R9"]),
("IV","ES202","Industry Coding Practices",2,1,2,4,U,4,["R3","R4"]),
("IV","DS204","Design and Analysis of Algorithms",3,0,0,3,K,3,["R6"]),
("IV","DS206","Computer Organization and Architecture",3,0,0,3,K,3,["R6"]),
("IV","DS207","Discrete Mathematics",2,1,0,3,K,3,["R6"]),
("IV","DS208","Web Enabled Technologies (Web 3.0)",2,1,2,4,K,4,[]),
("IV","DS212","Machine Learning",3,0,2,4,Rd,3,["R8"]),
("Summer","IP201","Summer Term / Internship Program - 1",0,0,0,5,K,5,[]),
("V","HS301","Constitution of India",0,0,0,0,K,0,["R9"]),
("V","Not listed","Elective-I (course/code not specified on page)",3,0,0,3,K,3,["R7"]),
("V","CR301","Power Skills - III",0,0,2,1,K,1,["R9"]),
("V","DS301","Metaheuristic Optimization Techniques",2,1,0,3,K,3,["R6"]),
("V","DS302","Computer Networks",3,0,2,4,K,4,["R6"]),
("V","DS303","Blockchain Technology",3,0,0,3,Rd,2,["R8"]),
("V","DS305","Data Wrangling and Visualization",2,0,2,3,U,3,["R3","R4"]),
("V","DS307","Computer Vision",3,0,0,3,Rd,0,["R7"]),
("V","PE1","Professional Elective (PE 1)",3,0,0,3,K,3,["R7"]),
("V","ADD-02","Generative AI Application Engineering: LLMs, retrieval and agents (proposed)",3,0,2,0,A,4,["R2","R3"]),
("VI","SP301","Special Project",0,0,6,3,K,3,["R10"]),
("VI","Not listed","Elective-II (course/code not specified on page)",3,0,0,3,K,3,["R7"]),
("VI","CR302","Power Skills - IV",0,0,2,1,K,1,["R9"]),
("VI","DS308","Big Data systems",3,0,0,3,Rd,0,["R7"]),
("VI","DS310","Deep Learning",2,1,2,4,U,4,["R3","R4"]),
("VI","DS312","Reinforcement Learning",3,0,0,3,K,3,["R2"]),
("VI","DS314","Fuzzy Logic and Rough Set Theory",2,1,0,3,K,3,["R6"]),
("VI","PE2","Professional Elective (PE 2)",3,0,0,3,K,3,["R7"]),
("VI","ADD-03","AI Output Verification and Governance (proposed)",2,1,0,0,A,3,["R3","R4"]),
]
keys=["sem","code","title","L","T","P","C","status","newC","reasons"]
# The student confirms the full programme total is 165 credits. The published
# itemized course map in this package accounts for 144 credits; the remaining
# 21 credits are included only as an aggregate KEEP line because the detailed
# cohort-specific course allocation was not supplied. Do not infer course names.
rows.append(("VII–VIII (aggregate)","UNMAPPED-21","Remaining programme credits (aggregate; detailed course allocation not mapped)",0,0,0,21,K,21,["R11"]))
courses=[dict(zip(keys,r)) for r in rows]

order=["I","II","III","IV","Summer","V","VI","VII–VIII (aggregate)"]
def off(c): return c["C"]
def prop(c): return c["newC"]
def aff(c):
    return {K:0,U:c["C"],Rd:c["C"]-c["newC"],A:c["newC"]}[c["status"]]
tot_off=sum(off(c) for c in courses); tot_prop=sum(prop(c) for c in courses)
add=sum(c["newC"] for c in courses if c["status"]==A)
red=sum(c["C"]-c["newC"] for c in courses if c["status"]==Rd)
upd=sum(c["C"] for c in courses if c["status"]==U)
affected=add+red+upd
keep_unch=sum(c["C"] for c in courses if c["status"]==K)
assert tot_off==165 and tot_prop==165 and add==red==10 and upd==15 and affected==35, (tot_off,tot_prop,add,red,upd)
reduced_official=sum(c["C"] for c in courses if c["status"]==Rd)
assert keep_unch+upd+reduced_official==tot_off  # partition of the official baseline

bysem={s:(sum(c["C"] for c in courses if c["sem"]==s), sum(c["newC"] for c in courses if c["sem"]==s)) for s in order}

reasons={
"R1":"HCLTech entry-level Generative AI listing is a provisional signal for Python, data processing and applied AI projects -> ADD-01 and UPDATE DS202. Verify the employer page before submission.",
"R2":"The small job-description sample suggests value in applied AI, model deployment and data workflows -> ADD-02. This is a proposal signal, not a claim about all 2030 jobs.",
"R3":"AI-assisted work should be paired with testing, evaluation, reproducibility and human review -> ADD-03 and UPDATE ES202, DS305 and DS310.",
"R4":"Database, data-wrangling and engineering-practice content can include access control, data validation, documentation and reproducible workflows -> UPDATE DS202, ES202, DS305 and DS310.",
"R5":"Foundational programming and data structures remain useful prerequisites for API design and automation -> KEEP ES105 and ES106; ADD-01 extends practice rather than replacing foundations.",
"R6":"Keep core mathematics, algorithms, operating systems, networks, architecture and data foundations. The small job sample cannot justify removing core fundamentals.",
"R7":"DS307 Computer Vision and DS308 Big Data systems are proposed to move from mandatory core to elective availability, not to be declared obsolete. Faculty and student validation is required.",
"R8":"Small one-credit reductions to ES102, DS201, DS212 and DS303 are low-confidence proposals. The core learning outcomes must be mapped before any reduction; absence from a few job ads is not proof of low value.",
"R9":"Basic sciences, mathematics, communication, Power Skills, Environmental Sciences and credit-free HS101/HS301 are left unchanged. Applicable academic regulations and any UGC/AICTE rules have not been independently checked.",
"R10":"SP301 Special Project hosts the Task 1 suggestion-box workflow capstone. Proposed semester totals for the itemized map remain 21/24/24/24/5/23/23; the published page prints 24-credit totals for Semesters V and VI while itemized lines sum to 23 in each.",
"R11":"The student confirms a 165-credit full-programme total. The detailed course allocation for the remaining 21 credits is not itemized in this map and is therefore kept unchanged as an aggregate, not assigned invented course codes.",
}

json.dump({"courses":courses,"reasons":reasons,"order":order},open(f"{R}/Task2/data/courses.json","w"),indent=1)

# ---------- course-map.md
L=["# Task 2 - Course map by semester\n",
"Baseline: **B.Tech CSE (Artificial Intelligence & Data Science), cohort 2023–2027**. The student confirms the full-programme total is **165 credits**. The published IFHE Hyderabad / IcfaiTech programme-structure page is used for the itemized course map (accessed 24 Oct 2026). The itemized rows here cover 144 credits; the remaining 21 credits are shown as an aggregate KEEP line because their detailed course allocation was not supplied. A separate cohort-specific Academic Regulations document was not supplied. Proposed changes are not official curriculum.\n",
"| Sem | Code | Course | L-T-P | Official C | Status | Proposed C | Reasons |","|---|---|---|---|---|---|---|---|"]
for s in order:
    for c in [x for x in courses if x["sem"]==s]:
        ltp = "-" if c["status"]==A else f'{c["L"]}-{c["T"]}-{c["P"]}'
        L.append(f'| {s} | {c["code"]} | {c["title"]} | {ltp} | {c["C"]} | {c["status"]} | {c["newC"]} | {", ".join(c["reasons"]) or "-"} |')
    L.append(f'| **{s}** | | *Semester total* | | **{bysem[s][0]}** | | **{bysem[s][1]}** | |')
L.append(f"\n**Full-programme total (student-confirmed): {tot_off} credits baseline; {tot_prop} proposed.** The itemized rows above include 144 credits from the public course map plus 21 aggregate credits marked KEEP because their detailed allocation was not supplied.\n")
L.append("The public page has a discrepancy between the printed and itemized totals for Semesters V and VI. This report preserves that discrepancy and does not invent missing course names. The separate cohort-specific Academic Regulations were not supplied.\n")
open(f"{R}/Task2/course-map.md","w").write("\n".join(L))

# ---------- credit-calculation.md
sens=[0,20,40]
C=["# Task 2 - Credit calculation\n","All figures are generated by `Task2/scripts/build_credit_tables.py` from `Task2/data/courses.json`; the arithmetic below can be re-checked by hand.\n",
"## 1. Baseline and scope\n","| Semester / component | Baseline credits | Proposed credits | Change |","|---|---|---|---|"]
for s in order: C.append(f"| {s} | {bysem[s][0]} | {bysem[s][1]} | {bysem[s][1]-bysem[s][0]:+d} |")
C.append(f"| **Full-programme total (student-confirmed)** | **{tot_off}** | **{tot_prop}** | **{tot_prop-tot_off:+d}** |")
C+=["\nThe itemized semesters total 144 credits (21 + 22 + 25 + 25 + 5 + 23 + 23). The student confirms the full-programme total is 165, leaving 21 credits not detailed in the itemized map; those are represented as an aggregate KEEP line, not assigned invented course codes.\n",
"The published page prints 24-credit totals for Semesters V and VI, while the itemized course rows each sum to 23. This discrepancy remains explicit. The 165-credit total is student-confirmed; the detailed allocation of the remaining 21 credits has not been independently mapped.\n",
"## 2. What counts as 'affected'\n",
"- ADD: all credits of the new course.\n- REDUCE: credits removed (old - new).\n- UPDATE: all credits of the course whose content changes (credit value unchanged).\n- KEEP: not affected.\n",
"| Component | Courses | Credits |","|---|---|---|",
"| ADD | ADD-01 (3), ADD-02 (4), ADD-03 (3) | 10 |",
"| REDUCE | DS307 (-3), DS308 (-3), ES102 (-1), DS201 (-1), DS212 (-1), DS303 (-1) | 10 |",
"| UPDATE | ES202 (4), DS202 (4), DS305 (3), DS310 (4) | 15 |",
f"| **Affected total** | | **{affected}** |\n",
f"Affected share = {affected} / {tot_off} = **{affected/tot_off*100:.1f}%** (target: roughly 20-25%).",
f"Structural change only (ADD + REDUCE, ignoring content updates) = {add+red} / {tot_off} = {(add+red)/tot_off*100:.1f}%.",
f"Net change: +{add} added - {red} removed = **0**, so the total stays {tot_off}.\n",
"## 3. Unchanged credits\n",
f"Unchanged (KEEP) = {keep_unch} credits, including the 21-credit aggregate line whose detailed course allocation was not supplied.\n"]
# show partition of the 165-credit total
retained_after_reduction=sum(c["newC"] for c in courses if c["status"]==Rd)
C.pop()
C+=[f"Partition of the {tot_off} programme credits: {keep_unch} unchanged (KEEP) + {upd} updated (UPDATE) + {red+retained_after_reduction} in reduced courses ({red} removed + {retained_after_reduction} retained) = {keep_unch+upd+red+retained_after_reduction}.\n",
"## 4. Denominator note\n",
f"Affected share = {affected}/165 = {affected/165*100:.1f}% against the student-confirmed full-programme total. The 21-credit remainder is marked KEEP pending an itemized course allocation. Structural changes only (ADD + REDUCE) are {add+red}/165 = {(add+red)/165*100:.1f}%.\n"]
C.append("## 5. Prerequisite checks\n")
C+=["| New/changed course | Sem | Prerequisites (proposed) | Satisfied earlier? |","|---|---|---|---|",
"| ADD-01 API Design, Integration and Python Automation | II | ES105 Computer Programming | Yes, Sem I |",
"| ADD-02 Generative AI Application Engineering | V | DS212 Machine Learning, DS202 DBMS, ADD-01 | Yes, Sem IV / III / II |",
"| ADD-03 AI Output Verification and Governance | VI | DS203 Artificial Intelligence; DS310 Deep Learning | Yes, Sem III / same semester |",
"| SP301 Special Project (capstone host) | VI | DS202, DS305, ADD-01 | Yes |",
"| DS307 / DS308 moved to elective pool | n/a | existing prerequisites unchanged (CBCS rule: choose if prerequisites met) | n/a |\n",
"Unverified: whether ES105/ES201 teach Python (the page gives no language). If they do not, ADD-01 carries the Python content and is the only place students first meet it."]
open(f"{R}/Task2/calculations/credit-calculation.md","w").write("\n".join(C))

# ---------- html
tpl=open(R+"/Task2/app/template.html").read()
open(f"{R}/Task2/app/index.html","w").write(tpl.replace("/*__DATA__*/null",json.dumps({"courses":courses,"reasons":reasons,"order":order})))
print("OK",tot_off,tot_prop,affected,round(affected/tot_off*100,1),bysem)
