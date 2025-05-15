<script>
  import { Route, Router, navigate } from "svelte-navigator";
  import Header from "./components/Header.svelte";
  import Footer from "./components/Footer.svelte";
  import NavItem from "./components/NavItem.svelte";

  import ColorChanger from "./routes/ColorChanger.svelte";
    import Colors from "./routes/Colors.svelte";
</script>

<main class="d-flex flex-column min-vh-100">
  <Header />
  <div class="px-5">
    <div class="alert alert-info">
      <b>Pixaddle이 무엇인가요?</b>
      <ul class="mb-0">
        <li>
            Pixaddle은 마인크래프트 지도에 그림을 그릴 때 사용할 수 있는 도구입니다.
        </li>
        <li>
          현재는 색상 변환 기능만을 제공하며,
          더 많은 기능이 추가될 예정입니다.
        </li>
        <li>
          사용 중 오류나 문제가 발생할 경우 <a href="https://github.com/itsk1mlot/Pixaddle/issues">Github Issue</a> 또는
          <a href="https://discord.gg/mxPnHvb3Zp">Discord</a>를 통해 알려주세요.
        </li>
        <li>
          후원하기: <a href="https://litt.ly/itskimlot_">https://litt.ly/itskimlot_</a>
        </li>
      </ul>
  </div>
  <Router>
    <ul class="nav nav-tabs mb-3">
      <NavItem href="/color-changer" text="색상 변환기" />
      <NavItem href="/colors" text="색상 목록" />
    </ul>
    <Route path="/color-changer" component={ColorChanger} />
    <Route path="/colors" component={Colors} />
    <Route>
      {navigate("/color-changer")}
    </Route>
  </Router>
</main>
<Footer />