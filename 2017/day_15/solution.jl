
function main()
    gen_a = 65
    gen_b = 8921
    count = 0
    gen_value(gen, factor) = (gen * factor) % 2147483647

    for _ = 1:40000000
        gen_a = gen_value(gen_a, 16807)
        gen_b = gen_value(gen_b, 48271)

        gen_a_low = gen_a & 0x0000FFFF
        gen_b_low = gen_b & 0x0000FFFF

        if gen_a_low == gen_b_low
            count += 1
        end
    end

    print(count)

end

main()