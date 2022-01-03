# Install puppet-lint
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'puppet_gem',
}
