import base64
html = base64.b64decode("PGgxPkJsb2d0cmFuczwvaDE+Cgo8cD5CbG9ndHJhbnPmmK/kuIDlpZfovYnmj5tibG9n6LOH5paZ5qC85byP55qE6ZaL5pS+5rqQ56K86Luf6auU55uu5YmN5pSv5o+077yaPC9wPgoKPGgyPuazqOaEj++8muW3suefpeWVj+mhjDwvaDI+Cgo8dWw+CjxsaT7nhKHlkI1YTUzmqpTmnInml6XmnJ/kuI3mraPnorrnmoTllY/poYzvvIjlpoIy5pyIMzHml6XvvIk8YnI+CkJsb2d0cmFuc+acg+iHquWLleippuWcluS/ruato++8iOWmguWwhzLmnIgzMeaXpeaUueeCujLmnIgyOOaXpe+8iTwvbGk+CjxsaT7lpoLljK/lh7rnmoRCbG9nZ2VyIEF0b20gWE1M54Sh5rOV5YWo6YOo5Yyv5YWlQmxvZ2dlcu+8iOWmguWMr+WFpTgwMOevh+WPquWHuuePvjMwMOevh++8iTxicj4K5Y+v6IO95piv55Sx5pa85paH56ug6aGe5Yil5pyJ54m55q6K56ym6Jmf77yM5Y+v6Kmm6JGX5L2/55So44CM5bel5YW377ya5riF6Zmk5omA5pyJ5paH56ug6aGe5Yil44CNPC9saT4KPC91bD4KCgo8cD7ntLDnr4Dlj4rlhbbku5blt7Lnn6XllY/poYzoqbPopos8YSBocmVmPSJodHRwOi8vbWlhb3V0MTcuZ2l0aHViLmlvL2Jsb2d0cmFucy9mYXEuaHRtbCI+RkFRPC9hPu+8jOWmgueEoeazleino+axuuatoei/jjxhIGhyZWY9Imh0dHA6Ly9taWFvdXQxNy5naXRodWIuaW8vYmxvZ3RyYW5zL3JlcG9ydC5odG1sIj7lm57loLHllY/poYw8L2E+44CCPC9wPgoKPGgyPuaUr+aPtOagvOW8jzwvaDI+Cgo8dWw+CjxsaT48YSBocmVmPSJodHRwOi8vd3d3Lm1vdmFibGV0eXBlLm9yZy9kb2N1bWVudGF0aW9uL2FwcGVuZGljZXMvaW1wb3J0LWV4cG9ydC1mb3JtYXQuaHRtbCI+TW92YWJsZVR5cGU8L2E+IOWMr+WFpeWPiuWMr+WHujwvbGk+CjxsaT48YSBocmVmPSJodHRwOi8vd3d3LndyZXRjaC5jYy9ibG9nLyI+54Sh5ZCN5bCP56uZWE1MPC9hPiDljK/lhaU8L2xpPgo8bGk+PGEgaHJlZj0iaHR0cDovL3d3dy5ibG9nZ2VyLmNvbSI+QmxvZ2dlciBBdG9tPC9hPiDljK/lh7o8L2xpPgo8L3VsPgoKCjxoMj7mm7TmlrDoqJjpjIQ8L2gyPgoKPHA+QmxvZ3RyYW5zIDEuMS4wICgyMDEzLzA5LzAzKTwvcD4KCjx1bD4KPGxpPuiHquWLleS/ruato+eEoeWQjVhNTOaqlOaXpeacn+mMr+iqpOeahOWVj+mhjO+8iOWmguiHquWLleWwhzIvMzHkv67mraPngroyLzI477yJPC9saT4KPGxpPuaWsOWinuOAjOW3peWFt++8mua4hemZpOaJgOacieaWh+eroOmhnuWIpeOAjeWKn+iDve+8iOeEoeazleWMr+WFpeaJgOacieaWh+eroOiHs0Jsb2dnZXLmmYLlj6/lmJfoqabkvb/nlKjvvIk8L2xpPgo8bGk+5L+u5q2j55WZ6KiA6ZmE5Yqg5pa86Yyv6Kqk5paH56ug55qEYnVnPC9saT4KPC91bD4KCgo8aDI+UnVubmluZyBCbG9ndHJhbnM8L2gyPgoKPGgzPldpbmRvd3M8L2gzPgoKPHA+VGhlcmUgaXMgb25seSBvZmZpY2lhbCBidWlsZCBmb3IgV2luZG93cyBzeXN0ZW0uClRoZSBXaW5kb3dzIGJ1aWxkIGlzIGF2YWlsYWJsZSBvbiBTb3VyY2VGb3JnZS4KVmlzaXQgPGEgaHJlZj0iaHR0cHM6Ly9zb3VyY2Vmb3JnZS5uZXQvcHJvamVjdC9zaG93ZmlsZXMucGhwP2dyb3VwX2lkPTIxMTU0OCI+cHJvamVjdCBkb3dubG9hZCBwYWdlPC9hPiB0byBnZXQgbmV3ZXN0IGJ1aWxkLjwvcD4KCjxoMz5MaW51eCBhbmQgTWFjPC9oMz4KCjxwPkxpbnV4IGFuZCBNYWMgdXNlciBjYW4gZ2V0IHRoZSBzb3VyY2UgY29kZSBhbmQgYnVpbGQgYnkgeW91cnNlbGYuClBsZWFzZSByZWZlciB0byA8c3Ryb25nPkJ1aWxkIGZyb20gU291cmNlPC9zdHJvbmc+IHNlY3Rpb24uPC9wPgoKPGgyPlVzYWdlPC9oMj4KCjxwPlBsZWFzZSByZWZlciB0byB0aGUgPGEgaHJlZj0iaHR0cDovL21pYW91dDE3LmdpdGh1Yi5jb20vYmxvZ3RyYW5zLyI+QmxvZ3RyYW5zIEhvbWVwYWdlPC9hPiAoVHJhZGl0aW9uYWwgQ2hpbmVzZSkuPC9wPgoKPGgyPkJ1aWxkIGZyb20gU291cmNlPC9oMj4KCjxwPlRoZSBjb2RlIGlzIG1haW5seSBob3N0ZWQgb24gPGEgaHJlZj0iaHR0cHM6Ly9naXRodWIuY29tL21pYW91dDE3L2Jsb2d0cmFucyI+R2l0aHViPC9hPgooVGhlcmUgaXMgYWxzbyBhIG1pcnJvciBvbiBTb3VyY2Vmb3JnZSwgYnV0IGl0J3Mgbm90IGFsd2F5cyB1cC10by1kYXRlKS48L3A+Cgo8cD5Zb3UgY2FuIGdldCB0aGUgc291cmNlIGNvZGUgdmlhIGdpdDo8L3A+Cgo8cHJlPjxjb2RlPmdpdCBjbG9uZSBnaXRAZ2l0aHViLmNvbTptaWFvdXQxNy9ibG9ndHJhbnMuZ2l0CjwvY29kZT48L3ByZT4KCjxwPm9yIGRpcmVjdGx5IGRvd25sb2FkIHRoZSA8YSBocmVmPSJodHRwczovL2dpdGh1Yi5jb20vbWlhb3V0MTcvYmxvZ3RyYW5zL3RhcmJhbGwvbWFzdGVyIj50YXJiYWxsPC9hPi48L3A+Cgo8aDM+RGVwZW5kZW5jaWVzPC9oMz4KCjxwPlBsZWFzZSBpbnN0YWxsIGZvbGxvd2luZyBpdGVtczo8L3A+Cgo8dWw+CjxsaT48YSBocmVmPSJodHRwOi8vd3d3LnB5dGhvbi5vcmcvIj5QeXRob248L2E+IDIuNiBvciBhYm92ZSAoYnV0IG5vdCAzLngpPC9saT4KPGxpPjxhIGhyZWY9Imh0dHA6Ly93d3cud3hweXRob24ub3JnLyI+d3hQeXRob248L2E+IDIuOCBvciBhYm92ZTwvbGk+CjxsaT48YSBocmVmPSJodHRwOi8vcHN5Y28uc291cmNlZm9yZ2UubmV0LyI+cHN5Y288L2E+IChvcHRpb25hbCk8L2xpPgo8L3VsPgoKCjxwPkFmdGVyIHRoYXQsIHlvdSBjYW4gZXhlY3V0ZSBCbG9nVHJhbnM6PC9wPgoKPHByZT48Y29kZT5weXRob24gYmxvZ3RyYW5zLnB5CjwvY29kZT48L3ByZT4KCjxoMz5UZXN0aW5nPC9oMz4KCjxwPkRvY3VtZW50IFRCRC4uPC9wPgoKPGgyPkxpZWNuc2U8L2gyPgoKPHA+QmxvZ3RyYW5zIGlzIHJlbGVhc2VkIHdpdGggTUlUIExJQ0VOU0UsIHNlZSBMSUNFTlNFIGZpbGUgZm9yIGRldGFpbHMuPC9wPgo=").decode("UTF-8")