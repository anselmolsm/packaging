pkgname=soletta
pkgver=1_beta6
pkgrel=2
checkdepends=()
conflicts=('soletta-git')
source=("https://github.com/solettaproject/soletta/archive/v$pkgver.tar.gz"
        "https://github.com/solettaproject/duktape-release/archive/v1_beta2.tar.gz")
md5sums=('8ef846a1e9def168ec90d4dfaa5b2c68'
         '69195d623d739158ecb055aeb02fd77b')

prepare() {
    cp -r duktape-release-1_beta2/* "$pkgname-$pkgver"/src/thirdparty/duktape/
}

build() {
	cd "$pkgname-$pkgver"
    make alldefconfig
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
