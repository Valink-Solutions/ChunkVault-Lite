<script>
	import Icon from '@iconify/svelte';
	import '../app.postcss';
</script>

<div class="flex flex-col min-h-full min-w-full">

	<div class="navbar bg-base-100 container mx-auto justify-center">
		<div class="navbar-center">
			<dif class="flex flex-row gap-1">
				<a href="/" class="font-metropolis-bold-italic text-2xl">ChunkVault</a>
				<div class="font-metropolis-semibold-italic badge badge-primary badge-sm">Lite</div>
			</dif>
		</div>
		<!-- <div class="navbar-end">
		  <div class="dropdown dropdown-end">
			<label tabindex="0" class="btn btn-hamburger lg:hidden">
			  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
			</label>
			<ul tabindex="0" class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
			  <li><a href="/">Item 1</a></li>
			  <li tabindex="0">
				<a class="justify-between">
				  Parent
				  <svg class="fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"/></svg>
				</a>
				<ul class="p-2">
				  <li><a href="/">Submenu 1</a></li>
				  <li><a href="/">Submenu 2</a></li>
				</ul>
			  </li>
			  <li><a href="/">Item 3</a></li>
			</ul>
		  </div>
		</div>
		<div class="navbar-end hidden lg:flex">
		  <ul class="menu menu-horizontal px-1">
			<li><a href="/">Item 1</a></li>
			<li tabindex="0">
			  <a href="/">
				Parent
				<svg class="fill-current" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"/></svg>
			  </a>
			  <ul class="p-2">
				<li><a href="/">Submenu 1</a></li>
				<li><a href="/">Submenu 2</a></li>
			  </ul>
			</li>
			<li><a href="/">Item 3</a></li>
		  </ul>
		</div> -->
	</div>

	<!-- <div class="navbar bg-base-100 container mx-auto">
		<div class="flex-1">
			<a href="/" class="font-metropolis-bold-italic text-2xl">ChunkVault</a>
		</div>
		<div class="flex-non">
			<div class="dropdown dropdown-end">
				<label tabindex="0" class="btn btn-hamburger text-2xl">
					<Icon icon="mdi:menu" />
				</label>
				<ul tabindex="0" class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52">
					<li>
					<a class="justify-between">
						Profile
						<span class="badge">New</span>
					</a>
					</li>
					<li><a>Settings</a></li>
					<li><a>Logout</a></li>
				</ul>
			</div>
		</div>
	</div> -->
	<div class="flex-grow container mx-auto">
		<slot />
	</div>
</div>
