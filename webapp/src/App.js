import React, { Component } from "react";
import "./App.css";
import comfortList from "./comfortList.json";
import { RaisedButton, TextField, FlatButton, AppBar, Chip } from "material-ui";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      no_s: 0,
      sid: 0,
      no_c: 0,
      cid: 0,
      subs: [],
      no_t: 0,
      no_g: 0,
      dow: 5,
      no_p: 6,
      maxNoClass: 6,
      comforts: comfortList.comforts,
      comfConst: [],
      completed: 0,
      helpopen: false,
      teachers: [],
      groups: [],
      teacherInput: "",
      groupInput: "",
    };
  }

  StartWebSocket = (_) => (_) => {
    this.ws = new WebSocket("ws://localhost:8888/ws");
    this.ws.onopen = () => {
      this.ws.send("knock");
    };

    this.ws.onmessage = (evt) => {
      var rec_msg = evt.data;
      if (rec_msg === "yes") {
        this.ws.send(JSON.stringify(this.state));
      } else {
        if (rec_msg.startsWith("[")) {
          this.setState({ result: JSON.parse(rec_msg) });
          this.setState({ completed: 1 });
        }
      }
    };
  };

  handleTeacherInputChange = (event) => {
    this.setState({ teacherInput: event.target.value });
    this.handleAddTeachers();
  };

  handleGroupInputChange = (event) => {
    this.setState({ groupInput: event.target.value });
    this.handleAddGroups();
  };

  handleAddTeachers = () => {
    const { teacherInput } = this.state;
    const teachers = teacherInput
      .split(",")
      .map((name) => name.trim())
      .filter((name) => name);
    this.setState({ teachers, no_t: teachers.length });
  };

  handleAddGroups = () => {
    const { groupInput } = this.state;
    const groups = groupInput
      .split(",")
      .map((name) => name.trim())
      .filter((name) => name);
    this.setState({ groups, no_g: groups.length });
  };

  render() {
    const { teachers, groups, teacherInput, groupInput } = this.state;

    return (
      <div className="App">
        <AppBar showMenuIconButton={false} title="Timetable Scheduler" />
        <h3>Classroom Parameters</h3>
        <div
          style={{
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.4)",
            padding: "20px",
            borderRadius: "8px",
            backgroundColor: "#fff",
            margin: "10px",
          }}
        >
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "auto 1fr auto 1fr",
              gap: "10px",
              alignItems: "center",
            }}
          >
            <label htmlFor="dow">No of working days in a week:</label>
            <TextField
              id="dow"
              type="number"
              onChange={this.handleChangedow}
              defaultValue={this.state.dow}
              min="1"
            />

            <label htmlFor="no_p">No of periods in a day:</label>
            <TextField
              id="no_p"
              type="number"
              onChange={this.handleChangeNo_p}
              defaultValue={this.state.no_p}
              min="1"
            />

            <label htmlFor="teacherInput">Teachers:</label>
            <TextField
              id="teacherInput"
              type="text"
              value={teacherInput}
              onChange={this.handleTeacherInputChange}
              placeholder="Enter names separated by commas"
            />

            <label htmlFor="groupInput">Groups:</label>
            <TextField
              id="groupInput"
              type="text"
              value={groupInput}
              onChange={this.handleGroupInputChange}
              placeholder="Enter names separated by commas"
            />
          </div>
        </div>
        <h3>Correctness constraints</h3>
        <RaisedButton
          onClick={this.handleAddClass}
          primary={true}
          label="Add a class"
        />
        <div
          style={{
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.4)",
            padding: "20px",
            borderRadius: "8px",
            backgroundColor: "#fff",
            margin: "10px",
          }}
        >
          {this.state.subs.map((subs, idx) => (
            <div key={subs.id}>
              <span className="constraintBar">
                <label>Subject id: {subs.id}</label>
                <TextField
                  id={`name` + subs.id}
                  type="text"
                  floatingLabelText={`Subject`}
                  onChange={this.handleChangeClassName(subs.id)}
                />
                <label>Teacher:</label> {this.createTlist(subs.id)}
                <label>Group:</label> {this.createGlist(subs.id)}
                <label>Hours:</label>{" "}
                <TextField
                  id={`n` + subs.id}
                  type="number"
                  onChange={this.handleChangeHour(subs.id)}
                  defaultValue={subs.dur}
                  min="1"
                />
                for {this.createNList(subs.id)} time.
                <FlatButton
                  onClick={this.handleRemoveClass(subs.id)}
                  secondary={true}
                  label="Remove"
                />
              </span>
            </div>
          ))}
        </div>
        <h3>Comfort constraints</h3>
        Add a comfort constraint: {this.listComfort()}
        <FlatButton
          onClick={this.handleAddComfort()}
          primary={true}
          label="Add"
        />
        <div
          style={{
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.4)",
            padding: "20px",
            borderRadius: "8px",
            backgroundColor: "#fff",
            margin: "10px",
          }}
        >
          {this.state.comfConst.map((cons, idx) => (
            <div key={idx}>
              {this.makeConstBody(cons)}
              <FlatButton
                onClick={this.handleRemoveComf(cons.id)}
                secondary={true}
                label="Remove"
              />
            </div>
          ))}
        </div>
        <div>
          <RaisedButton
            onClick={this.StartWebSocket(this.state)}
            primary={true}
            label="Send"
          />
        </div>
        <div className="ttable">{this.maketables()}</div>
      </div>
    );
  }

  maketables = () => {
    if (this.state.completed === 0) {
      return <span></span>;
    } else {
      var k = 0;
      var heads = [React.createElement("th", { key: k++ }, "X")];
      var nocol = 0;
      var rows = [];
      this.state.result.forEach((rowlist) => {
        var rowitems = [];
        rowlist.forEach((rowitem) => {
          var cellitems = [];
          if (typeof rowitem != "string")
            rowitem.forEach((cellitem) => {
              var thiss = this.state.subs.filter(
                (subs) => subs.id == cellitem[1]
              )[0].name;
              var thist = this.state.teachers[cellitem[0]];
              var thisg = this.state.groups[cellitem[2]];

              console.log({ thiss, thist, thisg });
              // cellitems.push(React.createElement('span', {key: k++}, "(" + thissub[0].name + ") "))
              cellitems.push(
                React.createElement(
                  "span",
                  { key: k++ },
                  "(" + thiss + " for " + thisg + " by " + thist + ") "
                )
              );
            });
          else
            cellitems.push(React.createElement("span", { key: k++ }, rowitem));
          // console.log(rowitem.length)
          rowitems.push(React.createElement("td", { key: k++ }, cellitems));
        });
        if (rowitems.length > nocol) nocol = rowitems.length;
        rows.push(React.createElement("tr", { key: k++ }, rowitems));
      });
      for (var i = 0; i < nocol - 1; i++) {
        heads.push(React.createElement("th", { key: k++ }, "Period " + i));
      }
      console.log("Making all tables");
      console.log(this.state.result);

      var ttable = React.createElement(
        "table",
        { border: 1, style: { display: "inline-block", margin: "5px" } },
        React.createElement("tbody", { key: k++ }, [
          React.createElement("tr", { key: k++ }, heads),
          rows,
        ])
      );
      return ttable;
    }
  };
  handleAddClass = () => {
    if (this.state.no_s < 100) {
      this.setState({
        subs: this.state.subs.concat([
          {
            id: this.state.sid,
            name: "",
            t: 0,
            g: 0,
            dur: 1,
            n: 0,
          },
        ]),
      });
      this.setState({ no_s: this.state.no_s + 1, sid: this.state.sid + 1 });
    }
  };

  handleChangeClassName = (s_id) => (evt) => {
    this.setState({
      subs: this.state.subs.map((subj) => {
        if (subj.id !== s_id) return subj;
        subj.name = evt.target.value;
        return subj;
      }),
    });
  };
  handleChangeHour = (s_id) => (evt) => {
    this.setState({
      subs: this.state.subs.map((subj) => {
        if (subj.id !== s_id) return subj;
        subj.dur = evt.target.value;
        return subj;
      }),
    });
  };
  createNList = (sid) => {
    var options = [];
    for (var i = 0; i < this.state.maxNoClass; i++) {
      var postf =
        i % 10 === 1 ? "st" : i % 10 === 2 ? "nd" : i % 10 === 3 ? "rd" : "th";
      options.push(
        React.createElement("option", { value: i, key: i }, i + postf)
      );
    }
    return <select onChange={this.setNConstraint(sid)}>{options}</select>;
  };
  handleRemoveClass = (idx) => () => {
    this.setState({ subs: this.state.subs.filter((subs) => subs.id !== idx) });
    this.setState({ no_s: this.state.no_s - 1 });
    // console.log("Rem" + idx)
  };
  setNConstraint = (sid) => (evt) => {
    this.setState({
      subs: this.state.subs.map((subj) => {
        if (subj.id !== sid) return subj;
        subj.n = evt.target.value;
        return subj;
      }),
    });
    console.log(" n constraint set for " + evt.target.value + " on " + sid);
  };
  handleChangeNo_t = (evt) => {
    this.setState({ no_t: evt.target.value });
  };
  handleChangeNo_g = (evt) => {
    this.setState({ no_g: evt.target.value });
  };
  handleChangedow = (evt) => {
    this.setState({ dow: evt.target.value });
  };
  handleChangeNo_p = (evt) => {
    this.setState({ no_p: evt.target.value });
  };
  handleRemoveComf = (comfid) => () => {
    this.setState({
      comfConst: this.state.comfConst.filter((comf) => comf.id !== comfid),
    });
    this.setState({ no_c: this.state.no_c - 1 });
  };
  handleAddComfort = () => (evt) => {
    var comfid = document.getElementById("comfList").value;
    var newcons = { id: this.state.cid, ctype: comfid };
    switch (comfid) {
      case "1":
        newcons["t"] = 0;
        newcons["p"] = 0;
        newcons["d"] = 0;
        break;
      case "2":
        newcons["t"] = 0;
        newcons["p"] = 0;
        newcons["d"] = 0;
        break;
      case "3":
        newcons["g"] = 0;
        newcons["d"] = 0;
        newcons["p"] = 0;
        break;
      case "4":
        newcons["g1"] = 0;
        newcons["g2"] = 0;
        break;
      case "5":
        newcons["t1"] = 0;
        newcons["t2"] = 0;
        break;
      case "6":
        newcons["t1"] = 0;
        newcons["t2"] = 0;
        break;
      case "7":
        newcons["t"] = 0;
        newcons["nd"] = 6;
        break;
      case "8":
        newcons["g"] = 0;
        newcons["d"] = 0;
        newcons["np"] = 1;
        break;
      case "9":
        newcons["t"] = 0;
        newcons["k"] = 1;
        break;
      case "10":
        newcons["s"] = 1;
        newcons["p"] = 1;
        newcons["mode"] = 0;
        break;
      case "11":
        newcons["s"] = 1;
        newcons["d"] = 0;
        newcons["mode"] = 0;
        break;
      case "12":
        newcons["s"] = 1;
        newcons["mode"] = 0;
        break;
      default:
        return false;
    }
    this.setState({ comfConst: this.state.comfConst.concat([newcons]) });
    this.setState({ no_c: this.state.no_c + 1, cid: this.state.cid + 1 });
  };

  setTeacherConstraint = (sid) => (evt) => {
    this.setState({
      subs: this.state.subs.map((subj) => {
        if (subj.id !== sid) return subj;
        subj.t = evt.target.value;
        return subj;
      }),
    });
    console.log(
      " teacher constraint set for " + evt.target.value + " on " + sid
    );
  };
  setGroupConstraint = (sid) => (evt) => {
    this.setState({
      subs: this.state.subs.map((subj) => {
        if (subj.id !== sid) return subj;
        subj.g = evt.target.value;
        return subj;
      }),
    });
    console.log("group constraint set for " + evt.target.value + " on " + sid);
  };
  setComfortParam = (cid, param) => (evt) => {
    this.setState({
      comfConst: this.state.comfConst.map((comf) => {
        if (comf.id !== cid) return comf;
        comf[param] = evt.target.value;
        return comf;
      }),
    });
    console.log(
      "comfort param set for " +
        evt.target.value +
        " on constraint " +
        cid +
        " as " +
        param
    );
  };

  makeConstBody = (cons) => {
    switch (cons.ctype) {
      case "1":
        return (
          <span>
            Teacher: {this.createTlistComf(cons)} prefers not to be scheduled on
            day: {this.createDlistComf(cons)} during period:{" "}
            {this.createPlistComf(cons)}{" "}
          </span>
        );
      case "2":
        return (
          <span>
            Teacher: {this.createTlistComf(cons)} prefers to be scheduled on
            day: {this.createDlistComf(cons)} during period:{" "}
            {this.createPlistComf(cons)}{" "}
          </span>
        );
      case "3":
        return (
          <span>
            Group : {this.createGlistComf(cons)} prefers not to be scheduled on
            day {this.createDlistComf(cons, "d", false)} during period{" "}
            {this.createPlistComf(cons, "p", false)}{" "}
          </span>
        );
      case "4":
        return (
          <span>
            Group : {this.createGlistComf(cons, "g1")} and Group :{" "}
            {this.createGlistComf(cons, "g2")} prefer not to be scheduled at the
            same time
          </span>
        );
      case "5":
        return (
          <span>
            Techers {this.createTlistComf(cons, "t1")} and{" "}
            {this.createTlistComf(cons, "t2")} prefer not to be scheduled at the
            same time
          </span>
        );
      case "6":
        return (
          <span>
            Techers {this.createTlistComf(cons, "t1")} and{" "}
            {this.createTlistComf(cons, "t2")} prefer to be scheduled at the
            same time
          </span>
        );
      case "7":
        return (
          <span>
            Teacher : {this.createTlistComf(cons)} prefers to have classes on
            atmost {this.createNoDComf(cons)} days
          </span>
        );
      case "8":
        return (
          <span>
            Group : {this.createGlistComf(cons)} prefers to have their classes
            limited to {this.createPlistComf(cons, "np")} periods on{" "}
            {this.createDlistComf(cons, "d", false)}
          </span>
        );
      case "9":
        return (
          <span>
            Teacher : {this.createTlistComf(cons)} prefers to have atmost{" "}
            {this.createPlistComf(cons, "k")} idle periods per day.
          </span>
        );
      case "10":
        return (
          <span>
            Subject : {this.createSubListComf(cons)} is preferred to be taught
            during period: {this.createPlistComf(cons, "p", false)}
          </span>
        );
      case "11":
        return (
          <span>
            Subject : {this.createSubListComf(cons)} is{" "}
            {this.askPreferComf(cons)} to be taught on{" "}
            {this.createDlistComf(cons)}
          </span>
        );
      case "12":
        return (
          <span>
            Subject : {this.createSubListComf(cons)} is{" "}
            {this.askPreferComf(cons)} to be taught on consecutive days
          </span>
        );
    }
  };
  askPreferComf(comf, paramName = "mode") {
    return (
      <select
        onChange={this.setComfortParam(comf.id, paramName)}
        value={comf[paramName]}
      >
        <option value="1" key="1">
          preferred
        </option>
        <option value="0" key="0">
          not preferred
        </option>
      </select>
    );
  }
  createNoDComf(comf, paramName = "nd") {
    return (
      <input
        type="number"
        min="1"
        max="7"
        onChange={this.setComfortParam(comf.id, paramName)}
        placeholder={comf[paramName]}
      />
    );
  }
  createSubListComf(comf, paramName = "s") {
    var options = [];
    for (var i = 0; i < this.state.no_s; i++) {
      options.push(
        React.createElement(
          "option",
          { value: this.state.subs[i].id, key: i },
          "id: " + this.state.subs[i].id
        )
      );
    }

    return (
      <select
        onChange={this.setComfortParam(comf.id, paramName)}
        value={comf[paramName]}
      >
        {options}
      </select>
    );
  }
  createTlistComf(comf, paramName = "t") {
    var options = [];
    for (var i = 0; i < this.state.no_t; i++) {
      options.push(React.createElement("option", { value: i, key: i }, i));
    }

    return (
      <select
        onChange={this.setComfortParam(comf.id, paramName)}
        value={comf[paramName]}
      >
        {options}
      </select>
    );
  }
  createGlistComf(comf, paramName = "g") {
    var options = [];
    for (var i = 0; i < this.state.no_g; i++) {
      options.push(React.createElement("option", { value: i, key: i }, i));
    }
    return (
      <select
        onChange={this.setComfortParam(comf.id, paramName)}
        value={comf[paramName]}
      >
        {options}
      </select>
    );
  }
  createDlistComf(comf, paramName = "d", alldays = true) {
    var options = [];
    if (alldays) {
      options = [
        React.createElement("option", { value: -1, key: 0 }, "All days"),
      ];
    }
    var days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    for (var i = 0; i < this.state.dow; i++) {
      options.push(
        React.createElement(
          "option",
          { value: i, key: i + 1 },
          i.toString() + " (" + days[i] + ")"
        )
      );
    }
    return (
      <select
        onChange={this.setComfortParam(comf.id, paramName)}
        value={comf[paramName]}
      >
        {options}
      </select>
    );
  }
  createPlistComf(comf, paramName = "p", allperiods = true) {
    var options = [];
    if (allperiods) {
      options = [
        React.createElement("option", { value: -1, key: 0 }, "All periods"),
      ];
    }
    for (var i = 0; i < this.state.no_p; i++) {
      options.push(React.createElement("option", { value: i, key: i + 1 }, i));
    }
    return (
      <select
        onChange={this.setComfortParam(comf.id, paramName)}
        value={comf[paramName]}
      >
        {options}
      </select>
    );
  }
  createTlist(sid) {
    var options = [];
    for (var i = 0; i < this.state.no_t; i++) {
      options.push(React.createElement("option", { value: i, key: i }, i));
    }

    return <select onChange={this.setTeacherConstraint(sid)}>{options}</select>;
  }
  createGlist(sid) {
    var options = [];
    for (var i = 0; i < this.state.no_g; i++) {
      options.push(React.createElement("option", { value: i, key: i }, i));
    }
    return <select onChange={this.setGroupConstraint(sid)}>{options}</select>;
  }
  listComfort() {
    var listElem = [];
    this.state.comforts.forEach((comfort) => {
      listElem.push(
        React.createElement(
          "option",
          { value: comfort.id, key: comfort.id },
          comfort.label
        )
      );
    });
    return (
      <select id="comfList" key={this.state.cid}>
        {listElem}
      </select>
    );
  }
  sendState = () => (evt) => {
    var req = new XMLHttpRequest();
    req.open("POST", "/input", false);
    req.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    req.send(JSON.stringify(this.state));
  };
}

export default App;
