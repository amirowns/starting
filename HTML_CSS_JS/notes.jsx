{
  /* comments are like this */
}

const JSX = (
  <div>
    <h1>
      Need every HTML added to be wrapped in parent div? Have to send a single
      element
    </h1>
  </div>
);

{
  /* need to render stuff in*/
}
ReactDOM.render(what_to_render, document.getElementById("id-goes-here"));

{
  /*stateless functional component recieve and render data but not manage or track changes to it, function that accepts props and return JSX*/
}
const MyComponent = function () {
  return <div className="customClass"> </div>;
};

{
  /*stateless component extends React.Component, but doesn't use internal state */
}
class MyComponent2 extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>Hi!</h1>
      </div>
    );
  }
}

{
  /*can also declare default props*/
}
MyComponent2.defaultProps = {
  location: "San Francisco",
};

{
  /*If you know the prop type you can set it to only receive that */
}
MyComponent.propTypes = { location: PropTypes.string.isRequired };

{
  /*stateful components/React components/components maintain their own internal state, better to minimize using these */
}
class StatefulComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: "Amir",
      visibility: false,
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    this.setState((state) => ({
      firstName: "Not Amir",
      visibility: !state.visibility,
    }));
  }
  render() {
    if (this.state.visibility) {
      return (
        <div>
          <button onClick={this.handleClick}>Click Me</button>
          <h1>{this.state.firstName}</h1>
        </div>
      );
    } else {
      return (
        <div>
          <button onClick={this.handleClick}>Click Me</button>
        </div>
      );
    }
  }
}
{
  /*passing props to es6 class components */
}
class App extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <Welcome name="chicken shit" />
      </div>
    );
  }
}

class Welcome extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <p>
          Hello, <strong>{this.props.name}</strong>!
        </p>
      </div>
    );
  }
}

{
  /*simple counter */
}
class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
    this.reset = this.reset.bind(this);
  }
  increment() {
    this.setState((state) => ({
      count: state.count + 1,
    }));
  }
  decrement() {
    this.setState((state) => ({
      count: state.count - 1,
    }));
  }
  reset() {
    this.setState({
      count: 0,
    });
  }
  render() {
    return (
      <div>
        <button className="inc" onClick={this.increment}>
          Increment!
        </button>
        <button className="dec" onClick={this.decrement}>
          Decrement!
        </button>
        <button className="reset" onClick={this.reset}>
          Reset
        </button>
        <h1>Current Count: {this.state.count}</h1>
      </div>
    );
  }
}

{
  /* input with submit button */
}
class MyForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: "",
      submit: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleChange(event) {
    this.setState({
      input: event.target.value,
    });
  }
  handleSubmit(event) {
    event.preventDefault();
    {
      /* needed to prevent the page from refreshing on submit*/
    }
    this.setState((state) => ({
      submit: state.input,
    }));
  }
  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input value={this.state.input} onChange={this.handleChange}></input>
          <button type="submit">Submit!</button>
        </form>
        <h1>{this.state.submit}</h1>
      </div>
    );
  }
}

{
  /*place api calls/server calls, event listeners in componentDidMount() */
}
class MyComponent3 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "",
    };
    this.handleEnter = this.handleEnter.bind(this);
    this.handleKeyPress = this.handleKeyPress.bind(this);
  }
  shouldComponentUpdate(nextProps, nextState) {
    console.log("Should I update?");
    return true;
  }
  componentDidUpdate() {
    console.log("Component re-rendered.");
  }
  componentDidMount() {
    document.addEventListener("keydown", this.handleKeyPress);
  }
  componentWillUnmount() {
    document.removeEventListener("keydown", this.handleKeyPress);
  }
  handleEnter() {
    this.setState((state) => ({
      message: state.message + "You pressed the enter key! ",
    }));
  }
  handleKeyPress(event) {
    if (event.keyCode === 13) {
      this.handleEnter();
    }
  }
  render() {
    return (
      <div>
        <h1>{this.state.message}</h1>
      </div>
    );
  }
}

{
  /*can add inline css, dont forget camelCase and {{}} 
  can also create a const with the styles and set the styles to this */
}
<div style={{ color: "red", fontSize: "72px" }}>Big Red</div>;

const styles = {
  color: "purple",
  fontSize: 40,
  border: "2px solid purple",
};

{
  /*can use && instead of if/else to keep code cleaner */
}
{
  this.state.display && <h1>Displayed!</h1>;
}

{
  /*render initial HTML for crawling webpage by using renderToString */
}
ReactDOMServer.renderToString(<App />);
