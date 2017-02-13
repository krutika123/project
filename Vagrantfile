# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'vagrant-env'

ANSIBLE_GROUPS = {
              "master" => ["node1"],
              "nodes" => ["node2", "node3", "node4","node5"],
              "all_groups:children" => ["master", "nodes"]
            }

Vagrant.configure(2) do |config|
	config.env.enable
	N=ENV['MY_VAR']
	puts "#{ENV['MY_VAR']}"
	(1..Integer(N)).each do |node_id|
    	config.vm.box = "bento/centos-7.1"
    	config.vm.define "node#{node_id}" do |node|
        	node.vm.network "private_network", ip: "192.168.33.#{9+node_id}"
        	node.vm.hostname = "node#{node_id}"

			if node_id==Integer(N)
				node.vm.provision :ansible do |ansible|
					ansible.limit = "all"
					ansible.playbook = "playbook.yml"
					ansible.groups = ANSIBLE_GROUPS
				end
        	end
        end
    end
end
