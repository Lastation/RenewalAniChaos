import Function as f;
import Character.Ekidona.Main as ekidonaMain;

var status = 0;

function contract(cp)
{
   if (Deaths(dwread_epd(204 * 12 + cp), AtLeast, 132, (210)) 
      && Deaths(dwread_epd(204 * 12 + cp), AtMost, 800, (210))
      && Deaths(cp, Exactly, 0, " `UniqueCoolTime"))
   {
      SetDeaths(dwread_epd(204 * 12 + cp), Subtract, 120, (210));
      SetDeaths(cp, SetTo, 3600, " `UniqueCoolTime");
   }
}

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            status = 0;
            SetSwitch("Recall - Ekidona", Set);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 101)
         {
            f.Voice_Routine(cp, 24);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 78)
         {
            f.Voice_Routine(cp, 25);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 63)
         {
            f.Voice_Routine(cp, 26);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (status == 0)
         {

         }
         else if (status == 1)
         {
            SetSwitch("Unique - Ekidona", Set);
         }
         SetSwitch("Recall - Ekidona", Clear);
         SetDeaths(cp, SetTo, 360, " `UniqueCoolTime");

         f.SkillEnd(cp);
      }

   }

   if (status == 0)
   {
      if (cp < 3)
      {
         f.stb.printAt(4, "\x13\x19계약\x04을 걸 플레이어를 선택해주십시오\x04");
         f.stb.printAt(5, "\x13\x04S : \x08P1\x04");
         f.stb.printAt(6, "\x13\x04C : \x0EP2\x04");
         f.stb.printAt(7, "\x13\x04A : \x0FP3\x04");

         if (Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
         {
            f.stb.print("\x13\x08P1 \x04지정\n");

            SetDeaths(cp, SetTo, 0, " `UniqueSkill");
            status = 1;
         }
         else if (Bring(cp, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
         {
            f.stb.print("\x13\x0EP2 \x04지정\n");

            SetDeaths(cp, SetTo, 1, " `UniqueSkill");
            status = 1;
         }
         else if (Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
         {
            f.stb.print("\x13\x0FP3 \x04지정\n");

            SetDeaths(cp, SetTo, 2, " `UniqueSkill");
            status = 1;
         }
      }
      else if (cp >= 3 && cp < 6)
      {
         f.stb.printAt(4, "\x13\x19계약\x04을 걸 플레이어를 선택해주십시오\x04");
         f.stb.printAt(5, "\x13\x04S : \x10P4\x04");
         f.stb.printAt(6, "\x13\x04C : \x11P5\x04");
         f.stb.printAt(7, "\x13\x04A : \x15P6\x04");

         if (Bring(cp, AtLeast, 1, "Protoss Scout", "[Skill]UseSkill"))
         {
            f.stb.print("\x13\x10P4 \x04지정\n");

            SetDeaths(cp, SetTo, 3, " `UniqueSkill");
            status = 1;
         }
         else if (Bring(cp, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill"))
         {
            f.stb.print("\x13\x11P5 \x04지정\n");

            SetDeaths(cp, SetTo, 4, " `UniqueSkill");
            status = 1;
         }
         else if (Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill"))
         {
            f.stb.print("\x13\x15P6 \x04지정\n");

            SetDeaths(cp, SetTo, 5, " `UniqueSkill");
            status = 1;
         }
      }


   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}